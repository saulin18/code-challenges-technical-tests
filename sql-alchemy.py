import math
from uuid import uuid4
from sqlalchemy import (
    ForeignKey,
    Integer,
    String,
    UUID,
    Float,
    delete,
    func,
    select,
    update,
)
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import List, Optional, Tuple, Dict, Any


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    student_name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)


engine = create_async_engine("sqlite+aiosqlite:///:memory:")

SessionFactory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def add_student(student: Student, db_session: AsyncSession) -> bool:
    db_session.add(student)
    await db_session.commit()
    return True


async def get_student(id: int, db_session: AsyncSession) -> Optional[Student]:
    return await db_session.get(Student, id)


async def update_student(id: int, email: str, db_session: AsyncSession) -> bool:
    student = await db_session.get(Student, id)
    if student:
        student.email = email
        await db_session.commit()
        return True
    return False


async def delete_student(id: int, db_session: AsyncSession) -> bool:
    student = await db_session.get(Student, id)
    if student:
        await db_session.delete(student)
        await db_session.commit()
        return True
    return False


class Item(Base):
    item_id: Mapped[UUID] = mapped_column(
        UUID, primary_key=True, default_factory=uuid4()
    )
    item_name: Mapped[str] = mapped_column(String, nullable=False)
    item_price: Mapped[float] = mapped_column(Float, nullable=False)
    item_quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    __tablename__ = "items"


class User(Base):
    user_id: Mapped[UUID] = mapped_column(
        UUID, primary_key=True, default_factory=uuid4()
    )
    user_name: Mapped[str] = mapped_column(String, nullable=False)
    user_email: Mapped[str] = mapped_column(String, nullable=False)

    __tablename__ = "users"


class Order(Base):
    order_id: Mapped[UUID] = mapped_column(
        UUID, primary_key=True, default_factory=uuid4()
    )
    user_id: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("users.user_id"), nullable=False
    )
    item_id: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("items.item_id"), nullable=False
    )
    order_quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    __tablename__ = "orders"


async def retrieve_items_by_price(price: float, db_session: AsyncSession) -> List[Item]:
    result = await db_session.scalars(select(Item).where(Item.item_price > price))
    return result.all()


async def update_item_quantity(
    quantity: int, item_name: str, db_session: AsyncSession
) -> bool:
    await db_session.execute(
        update(Item).where(Item.item_name == item_name).values(item_quantity=quantity)
    )
    await db_session.commit()
    return True


async def create_order(
    user_id: UUID, item_id: UUID, quantity: int, db_session: AsyncSession
) -> bool:
    order = Order(user_id=user_id, item_id=item_id, order_quantity=quantity)
    db_session.add(order)
    await db_session.commit()
    return True


async def retrieve_orders_by_user(
    user_id: UUID, db_session: AsyncSession
) -> List[Order]:
    result = await db_session.scalars(select(Order).where(Order.user_id == user_id))
    return result.all()


async def total_cost_of_orders_of_a_user(
    user_id: UUID, db_session: AsyncSession
) -> float:
    result = await db_session.scalars(
        func.sum(Order.order_quantity * Item.item_price)
        .where(Order.user_id == user_id)
        .join(Item, Order.item_id == Item.item_id)
    )
    return result.all()


async def top_2_products_by_sales(db_session: AsyncSession) -> List[Item]:
    query = (
        select(Item.item_name, func.sum(Order.order_quantity))
        .group_by(Item.item_id)
        .join(Order, Order.item_id == Item.item_id)
        .order_by(func.sum(Order.order_quantity).desc())
        .limit(2)
    )
    result = await db_session.scalars(query)
    return result.all()


async def delete_order_record(order_id: UUID, db_session: AsyncSession) -> bool:
    order: Optional[Order] = await db_session.scalar(
        select(Order).where(Order.order_id == order_id)
    )

    if not order:
        return False

    delete_order_query = delete(Order).where(Order.order_id)

    order_item: Optional[Item] = await db_session.get(Item, order.item_id)

    if not order_item:
        return False

    update_item_quantity_query = (
        update(Item)
        .where(Item.item_id == order_item.item_id)
        .values(item_quantity=order_item.item_quantity + order.order_quantity)
    )

    await db_session.execute(update_item_quantity_query)
    await db_session.execute(delete_order_query)

    await db_session.commit()
    return True


async def get_stats(db_session: AsyncSession) -> Tuple[int, float, float, float, float]:
    get_total_orders_query = select(func.count(Order))

    get_total_sales_amount_query = select(
        func.sum(Order.order_quantity * Item.item_price).join(
            Item, Order.item_id == Item.item_id
        )
    )

    get_minimum_item_price_query = select(func.min(Item.item_price))

    get_maximum_item_price_query = select(func.max(Item.item_price))

    get_average_order_quantity_query = select(func.avg(Order.order_quantity))

    total_orders = await db_session.scalar(get_total_orders_query)
    total_sales_amount = await db_session.scalar(get_total_sales_amount_query)
    minimum_item_price = await db_session.scalar(get_minimum_item_price_query)
    maximum_item_price = await db_session.scalar(get_maximum_item_price_query)
    average_order_quantity = await db_session.scalar(get_average_order_quantity_query)
    return (
        total_orders,
        total_sales_amount,
        minimum_item_price,
        maximum_item_price,
        average_order_quantity,
    )


async def update_user(
    user_id: UUID, user_name: str, user_email: str, db_session: AsyncSession
) -> bool:
    async with db_session.begin():
        stmt = select(User).where(User.user_id == user_id).with_for_update()
        if user := await db_session.scalar(stmt):
            user.user_name = user_name
            user.user_email = user_email
            return True
        return False


async def get_all_users_paginated(page: int, page_size: int, db_session: AsyncSession) -> Dict[str, Any]:
    if page < 1:
        raise ValueError("Page must be greater than 0")

    stmt = (
        select(User, func.count(User).over().label("total_results"))
        .limit(page_size)
        .offset((page - 1) * page_size)
        # with fetch will be .fetch(page_size) instead of limit
    )

    results = await db_session.execute(stmt)
    rows: List[Tuple[User, int]] = results.all()

    if not rows:
        return {
            "data": [],
            "total_pages": 0,
            "total_results": 0,
        }

    total_results = rows[0][1]

    total_pages = math.ceil(total_results / page_size)

    if total_pages < page:
        raise ValueError("Page is out of range")

    return {
        "data": [user[0] for user in rows],
        "total_pages": total_pages,
        "total_results": total_results,
    }

