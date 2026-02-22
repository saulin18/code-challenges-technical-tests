import inspect
import math
from datetime import datetime
import os
from uuid import uuid4
from sqlalchemy import (
    Boolean,
    DateTime,
    ExecutionContext,
    ForeignKey,
    Integer,
    String,
    UUID,
    Float,
    create_engine,
    delete,
    event,
    func,
    select,
    update,
)
from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import orm
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.horizontal_shard import ShardedSession, set_shard_id
from sqlalchemy.orm import DeclarativeBase, selectinload, sessionmaker
from sqlalchemy.orm import immediateload
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import operators
from sqlalchemy.sql import visitors
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)
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
    item_id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default_factory=uuid4)
    item_name: Mapped[str] = mapped_column(String, nullable=False)
    item_price: Mapped[float] = mapped_column(Float, nullable=False)
    item_quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    __tablename__ = "items"


class User(Base):
    user_id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default_factory=uuid4)
    user_name: Mapped[str] = mapped_column(String, nullable=False)
    user_email: Mapped[str] = mapped_column(String, nullable=False)

    __tablename__ = "users"


class Order(Base):
    order_id: Mapped[UUID] = mapped_column(
        UUID, primary_key=True, default_factory=uuid4
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
        select(func.sum(Order.order_quantity * Item.item_price))
        .select_from(Order)
        .join(Item, Order.item_id == Item.item_id)
        .where(Order.user_id == user_id)
    )

    return result.first()


async def top_2_products_by_sales(db_session: AsyncSession):
    query = (
        select(Item.item_name, func.sum(Order.order_quantity))
        .group_by(Item.item_id)
        .join(Order, Order.item_id == Item.item_id)
        .order_by(func.sum(Order.order_quantity).desc())
        .limit(2)
    )
    result = await db_session.execute(query)
    return result.all()


async def delete_order_record(order_id: UUID, db_session: AsyncSession) -> bool:
    order: Optional[Order] = await db_session.scalar(
        select(Order).where(Order.order_id == order_id)
    )

    if not order:
        return False

    delete_order_query = delete(Order).where(Order.order_id == order_id)

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
    get_total_orders_query = select(func.count(Order.order_id))

    get_total_sales_amount_query = select(
        func.sum(Order.order_quantity * Item.item_price)
        .select_from(Order)
        .join(Item, Order.item_id == Item.item_id)
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


async def get_all_users_paginated(
    page: int, page_size: int, db_session: AsyncSession
) -> Dict[str, Any]:
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


###
##
## SQLAlchemy Sharding 4 examples by the documentation
## 1. Asyncio with multiple databases https://docs.sqlalchemy.org/en/20/_modules/examples/sharding/asyncio.html
## 2. Separate schemas single database https://docs.sqlalchemy.org/en/20/_modules/examples/sharding/separate_schema_translates.html
## 3. Separate databases https://docs.sqlalchemy.org/en/20/_modules/examples/sharding/separate_databases.html
## 4. Separate tables with single database https://docs.sqlalchemy.org/en/20/_modules/examples/sharding/separate_tables.html
###


echo = True
db1 = create_async_engine("sqlite+aiosqlite://", echo=echo)
db2 = create_async_engine("sqlite+aiosqlite://", echo=echo)
db3 = create_async_engine("sqlite+aiosqlite://", echo=echo)
db4 = create_async_engine("sqlite+aiosqlite://", echo=echo)

Session = async_sessionmaker(
    sync_session_class=AsyncSession,
    expire_on_commit=False,
    shards={
        "shard1": db1,
        "shard2": db2,
        "shard3": db3,
        "shard4": db4,
    },
)


# we need a way to create identifiers which are unique across all databases.
# one easy way would be to just use a composite primary key, where  one value
# is the shard id.  but here, we'll show something more "generic", an id
# generation function.  we'll use a simplistic "id table" stored in database
# #1.  Any other method will do just as well; UUID, hilo, application-specific,
# etc.

ids = Table("ids", Base.metadata, Column("nextid", Integer, nullable=False))


def id_generator(ctx):
    # id_generator is run within a "synchronous" context, where
    # we use an implicit-await API that will convert back to explicit await
    # calls when it reaches the driver.
    with db1.sync_engine.begin() as conn:
        nextid = conn.scalar(ids.select().with_for_update())
        conn.execute(ids.update().values({ids.c.nextid: ids.c.nextid + 1}))
    return nextid


# table setup.  we'll store a lead table of continents/cities, and a secondary
# table storing locations. a particular row will be placed in the database
# whose shard id corresponds to the 'continent'.  in this setup, secondary rows
# in 'weather_reports' will be placed in the same DB as that of the parent, but
# this can be changed if you're willing to write more complex sharding
# functions.


class WeatherLocation(Base):
    __tablename__ = "weather_locations"

    id: Mapped[int] = mapped_column(primary_key=True, default=id_generator)
    continent: Mapped[str]
    city: Mapped[str]

    reports: Mapped[list["Report"]] = relationship(back_populates="location")

    def __init__(self, continent: str, city: str):
        self.continent = continent
        self.city = city


class Report(Base):
    __tablename__ = "weather_reports"

    id: Mapped[int] = mapped_column(primary_key=True)
    location_id: Mapped[int] = mapped_column(ForeignKey("weather_locations.id"))
    temperature: Mapped[float]
    report_time: Mapped[datetime] = mapped_column(default=datetime.now)

    location: Mapped[WeatherLocation] = relationship(back_populates="reports")

    def __init__(self, temperature: float):
        self.temperature = temperature


# step 5. define sharding functions.

# we'll use a straight mapping of a particular set of "country"
# attributes to shard id.
shard_lookup = {
    "North America": "north_america",
    "Asia": "asia",
    "Europe": "europe",
    "South America": "south_america",
}


def shard_chooser(mapper, instance, clause=None):
    """shard chooser.

    looks at the given instance and returns a shard id
    note that we need to define conditions for
    the WeatherLocation class, as well as our secondary Report class which will
    point back to its WeatherLocation via its 'location' attribute.

    """
    if isinstance(instance, WeatherLocation):
        return shard_lookup[instance.continent]
    else:
        return shard_chooser(mapper, instance.location)


def identity_chooser(mapper, primary_key, *, lazy_loaded_from, **kw):
    """identity chooser.

    given a primary key, returns a list of shards
    to search.  here, we don't have any particular information from a
    pk so we just return all shard ids. often, you'd want to do some
    kind of round-robin strategy here so that requests are evenly
    distributed among DBs.

    """
    if lazy_loaded_from:
        # if we are in a lazy load, we can look at the parent object
        # and limit our search to that same shard, assuming that's how we've
        # set things up.
        return [lazy_loaded_from.identity_token]
    else:
        return ["north_america", "asia", "europe", "south_america"]


def execute_chooser(context):
    """statement execution chooser.

    this also returns a list of shard ids, which can just be all of them. but
    here we'll search into the execution context in order to try to narrow down
    the list of shards to SELECT.

    """
    ids = []

    # we'll grab continent names as we find them
    # and convert to shard ids
    for column, operator, value in _get_select_comparisons(context.statement):
        # "shares_lineage()" returns True if both columns refer to the same
        # statement column, adjusting for any annotations present.
        # (an annotation is an internal clone of a Column object
        # and occur when using ORM-mapped attributes like
        # "WeatherLocation.continent"). A simpler comparison, though less
        # accurate, would be "column.key == 'continent'".
        if column.shares_lineage(WeatherLocation.__table__.c.continent):
            if operator == operators.eq:
                ids.append(shard_lookup[value])
            elif operator == operators.in_op:
                ids.extend(shard_lookup[v] for v in value)

    if len(ids) == 0:
        return ["north_america", "asia", "europe", "south_america"]
    else:
        return ids


def _get_select_comparisons(statement):
    """Search a Select or Query object for binary expressions.

    Returns expressions which match a Column against one or more
    literal values as a list of tuples of the form
    (column, operator, values).   "values" is a single value
    or tuple of values depending on the operator.

    """
    binds = {}
    clauses = set()
    comparisons = []

    def visit_bindparam(bind):
        # visit a bind parameter.

        value = bind.effective_value
        binds[bind] = value

    def visit_column(column):
        clauses.add(column)

    def visit_binary(binary):
        if binary.left in clauses and binary.right in binds:
            comparisons.append((binary.left, binary.operator, binds[binary.right]))

        elif binary.left in binds and binary.right in clauses:
            comparisons.append((binary.right, binary.operator, binds[binary.left]))

    # here we will traverse through the query's criterion, searching
    # for SQL constructs.  We will place simple column comparisons
    # into a list.
    if statement.whereclause is not None:
        visitors.traverse(
            statement.whereclause,
            {},
            {
                "bindparam": visit_bindparam,
                "binary": visit_binary,
                "column": visit_column,
            },
        )
    return comparisons


# further configure create_session to use these functions
Session.configure(
    shard_chooser=shard_chooser,
    identity_chooser=identity_chooser,
    execute_chooser=execute_chooser,
)


async def setup():
    # create tables
    for db in (db1, db2, db3, db4):
        async with db.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    # establish initial "id" in db1
    async with db1.begin() as conn:
        await conn.execute(ids.insert(), {"nextid": 1})


async def main():
    await setup()

    # save and load objects!

    tokyo = WeatherLocation("Asia", "Tokyo")
    newyork = WeatherLocation("North America", "New York")
    toronto = WeatherLocation("North America", "Toronto")
    london = WeatherLocation("Europe", "London")
    dublin = WeatherLocation("Europe", "Dublin")
    brasilia = WeatherLocation("South America", "Brasila")
    quito = WeatherLocation("South America", "Quito")

    tokyo.reports.append(Report(80.0))
    newyork.reports.append(Report(75))
    quito.reports.append(Report(85))

    async with Session() as sess:
        sess.add_all([tokyo, newyork, toronto, london, dublin, brasilia, quito])

        await sess.commit()

        t = await sess.get(
            WeatherLocation,
            tokyo.id,
            options=[immediateload(WeatherLocation.reports)],
        )
        assert t.city == tokyo.city
        assert t.reports[0].temperature == 80.0

        # select across shards
        asia_and_europe = (
            await sess.execute(
                select(WeatherLocation).filter(
                    WeatherLocation.continent.in_(["Europe", "Asia"])
                )
            )
        ).scalars()

        assert {c.city for c in asia_and_europe} == {
            "Tokyo",
            "London",
            "Dublin",
        }

        # optionally set a shard id for the query and all related loaders
        north_american_cities_w_t = (
            await sess.execute(
                select(WeatherLocation)
                .filter(WeatherLocation.city.startswith("T"))
                .options(set_shard_id("north_america"))
            )
        ).scalars()

        # Tokyo not included since not in the north_america shard
        assert {c.city for c in north_american_cities_w_t} == {
            "Toronto",
        }

        # the Report class uses a simple integer primary key.  So across two
        # databases, a primary key will be repeated.  The "identity_token"
        # tracks in memory that these two identical primary keys are local to
        # different shards.
        newyork_report = newyork.reports[0]
        tokyo_report = tokyo.reports[0]

        assert inspect(newyork_report).identity_key == (
            Report,
            (1,),
            "north_america",
        )
        assert inspect(tokyo_report).identity_key == (Report, (1,), "asia")

        # the token representing the originating shard is also available
        # directly
        assert inspect(newyork_report).identity_token == "north_america"
        assert inspect(tokyo_report).identity_token == "asia"


## Sharding with multiple schemas

engine = create_engine("sqlite://", echo=echo)


with engine.connect() as conn:
    # use attached databases on sqlite to get "schemas"
    for i in range(1, 5):
        if os.path.exists("schema_%s.db" % i):
            os.remove("schema_%s.db" % i)
        conn.exec_driver_sql('ATTACH DATABASE "schema_%s.db" AS schema_%s' % (i, i))

db1 = engine.execution_options(schema_translate_map={None: "schema_1"})
db2 = engine.execution_options(schema_translate_map={None: "schema_2"})
db3 = engine.execution_options(schema_translate_map={None: "schema_3"})
db4 = engine.execution_options(schema_translate_map={None: "schema_4"})

Session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=ShardedSession,
    shards={
        "shard1": db1,
        "shard2": db2,
        "shard3": db3,
        "shard4": db4,
    },
    shard_chooser=shard_chooser,
    identity_chooser=identity_chooser,
    execute_chooser=execute_chooser,
)


### Separate databases

db1 = create_engine("sqlite://", echo=echo)
db2 = create_engine("sqlite://", echo=echo)
db3 = create_engine("sqlite://", echo=echo)
db4 = create_engine("sqlite://", echo=echo)

Session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=ShardedSession,
    shards={
        "shard1": db1,
        "shard2": db2,
        "shard3": db3,
        "shard4": db4,
    },
)


engine = create_engine("sqlite://", echo=echo)

db1 = engine.execution_options(table_prefix="north_america")
db2 = engine.execution_options(table_prefix="asia")
db3 = engine.execution_options(table_prefix="europe")
db4 = engine.execution_options(table_prefix="south_america")


@event.listens_for(engine, "before_cursor_execute", retval=True)
def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    table_prefix = context.execution_options.get("table_prefix", None)
    if table_prefix:
        statement = statement.replace("_prefix_", table_prefix)
    return statement, parameters


# create session function.  this binds the shard ids
# to databases within a ShardedSession and returns it.
Session = sessionmaker(
    class_=ShardedSession,
    shards={
        "north_america": db1,
        "asia": db2,
        "europe": db3,
        "south_america": db4,
    },
)


# table setup.  we'll store a lead table of continents/cities, and a secondary
# table storing locations. a particular row will be placed in the database
# whose shard id corresponds to the 'continent'.  in this setup, secondary rows
# in 'weather_reports' will be placed in the same DB as that of the parent, but
# this can be changed if you're willing to write more complex sharding
# functions.


class WeatherLocation(Base):
    __tablename__ = "_prefix__weather_locations"

    id: Mapped[int] = mapped_column(primary_key=True, default=id_generator)
    continent: Mapped[str]
    city: Mapped[str]

    reports: Mapped[list[Report]] = relationship(back_populates="location")

    def __init__(self, continent: str, city: str):
        self.continent = continent
        self.city = city


class Report(Base):
    __tablename__ = "_prefix__weather_reports"

    id: Mapped[int] = mapped_column(primary_key=True)
    location_id: Mapped[int] = mapped_column(
        ForeignKey("_prefix__weather_locations.id")
    )
    temperature: Mapped[float]
    report_time: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.now
    )

    location: Mapped[WeatherLocation] = relationship(back_populates="reports")

    def __init__(self, temperature: float):
        self.temperature = temperature


"""Illustrates a global criteria applied to entities of a particular type.

The example here is the "public" flag, a simple boolean that indicates
the rows are part of a publicly viewable subcategory.  Rows that do not
include this flag are not shown unless a special option is passed to the
query.

Uses for this kind of recipe include tables that have "soft deleted" rows
marked as "deleted" that should be skipped, rows that have access control rules
that should be applied on a per-request basis, etc.


"""


@event.listens_for(Session, "do_orm_execute")
def _add_filtering_criteria(execute_state):
    """Intercept all ORM queries.   Add a with_loader_criteria option to all
    of them.

    This option applies to SELECT queries and adds a global WHERE criteria
    (or as appropriate ON CLAUSE criteria for join targets)
    to all objects of a certain class or superclass.

    """

    # the with_loader_criteria automatically applies itself to
    # relationship loads as well including lazy loads.   So if this is
    # a relationship load, assume the option was set up from the top level
    # query.

    if (
        not execute_state.is_column_load
        and not execute_state.is_relationship_load
        and not execute_state.execution_options.get("include_private", False)
    ):
        execute_state.statement = execute_state.statement.options(
            orm.with_loader_criteria(
                HasPrivate,
                lambda cls: cls.public == True,
                include_aliases=True,
            )
        )


class HasPrivate:
    """Mixin that identifies a class as having private entities"""

    public = Column(Boolean, nullable=False)


class User(HasPrivate, Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    addresses = relationship("Address", back_populates="user")


class Address(HasPrivate, Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="addresses")


engine = create_engine("sqlite://", echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
sess = Session()
sess.add_all(
    [
        User(
            name="u1",
            public=True,
            addresses=[
                Address(email="u1a1", public=True),
                Address(email="u1a2", public=True),
            ],
        ),
        User(
            name="u2",
            public=True,
            addresses=[
                Address(email="u2a1", public=False),
                Address(email="u2a2", public=True),
            ],
        ),
        User(
            name="u3",
            public=False,
            addresses=[
                Address(email="u3a1", public=False),
                Address(email="u3a2", public=False),
            ],
        ),
        User(
            name="u4",
            public=False,
            addresses=[
                Address(email="u4a1", public=False),
                Address(email="u4a2", public=True),
            ],
        ),
        User(
            name="u5",
            public=True,
            addresses=[
                Address(email="u5a1", public=True),
                Address(email="u5a2", public=False),
            ],
        ),
    ]
)
sess.commit()
# now querying Address or User objects only gives us the public ones
for u1 in sess.query(User).options(orm.selectinload(User.addresses)):
    assert u1.public
    # the addresses collection will also be "public only", which works
    # for all relationship loaders including joinedload
    for address in u1.addresses:
        assert address.public
# works for columns too
cols = (
    sess.query(User.id, Address.id)
    .join(User.addresses)
    .order_by(User.id, Address.id)
    .all()
)
assert cols == [(1, 1), (1, 2), (2, 4), (5, 9)]
cols = (
    sess.query(User.id, Address.id)
    .join(User.addresses)
    .order_by(User.id, Address.id)
    .execution_options(include_private=True)
    .all()
)
assert cols == [
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (3, 6),
    (4, 7),
    (4, 8),
    (5, 9),
    (5, 10),
]
# count all public addresses
assert sess.query(Address).count() == 5
# count all addresses public and private
assert sess.query(Address).execution_options(include_private=True).count() == 10
# load an Address that is public, but its parent User is private
# (2.0 style query)
a1 = sess.execute(select(Address).filter_by(email="u4a2")).scalar()
# assuming the User isn't already in the Session, it returns None
assert a1.user is None
# however, if that user is present in the session, then a many-to-one
# does a simple get() and it will be present
sess.expire(a1, ["user"])
u1 = sess.execute(
    select(User).filter_by(name="u4").execution_options(include_private=True)
).scalar()
assert a1.user is u1


"""Illustrates a custom per-query criteria that will be applied
to selected entities.


"""

from functools import partial


class HasTemporal:
    """Mixin that identifies a class as having a timestamp column"""

    timestamp = Column(
        DateTime,
        default=partial(datetime.datetime.now, datetime.timezone.utc),
        nullable=False,
    )


def temporal_range(range_lower, range_upper):
    return orm.with_loader_criteria(
        HasTemporal,
        lambda cls: cls.timestamp.between(range_lower, range_upper),
        include_aliases=True,
    )
    
@event.listens_for(Session, "do_orm_execute")
def _add_temporal_range(execute_state):
    """Intercept all ORM queries.   Add a with_loader_criteria option to all
    of them.

    This option applies to SELECT queries and adds a global WHERE criteria
    (or as appropriate ON CLAUSE criteria for join targets)
    to all objects of a certain class or superclass.

    """
    if execute_state.is_relationship_load:
        execute_state.statement = execute_state.statement.options(
            temporal_range(
                execute_state.execution_options.get("range_lower"),
                execute_state.execution_options.get("range_upper"),
            )
        )


class Parent(HasTemporal, Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    children = relationship("Child")


class Child(HasTemporal, Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("parent.id"), nullable=False)


engine = create_engine("sqlite://", echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
sess = Session()
c1, c2, c3, c4, c5 = [
    Child(timestamp=datetime.datetime(2009, 10, 15, 12, 00, 00)),
    Child(timestamp=datetime.datetime(2009, 10, 17, 12, 00, 00)),
    Child(timestamp=datetime.datetime(2009, 10, 20, 12, 00, 00)),
    Child(timestamp=datetime.datetime(2009, 10, 12, 12, 00, 00)),
    Child(timestamp=datetime.datetime(2009, 10, 17, 12, 00, 00)),
]
p1 = Parent(
    timestamp=datetime.datetime(2009, 10, 15, 12, 00, 00),
    children=[c1, c2, c3],
)
p2 = Parent(
    timestamp=datetime.datetime(2009, 10, 17, 12, 00, 00),
    children=[c4, c5],
)
sess.add_all([p1, p2])
sess.commit()
# use populate_existing() to ensure the range option takes
# place for elements already in the identity map
parents = (
    sess.query(Parent)
    .populate_existing()
    .options(
        temporal_range(
            range_lower=datetime.datetime(2009, 10, 16, 12, 00, 00),
            range_upper=datetime.datetime(2009, 10, 18, 12, 00, 00),
        )
    )
    .all()
)
assert parents[0] == p2
assert parents[0].children == [c5]
sess.expire_all()
# try it with eager load
parents = (
    sess.query(Parent)
    .options(
        temporal_range(
            range_lower=datetime.datetime(2009, 10, 16, 12, 00, 00),
            range_upper=datetime.datetime(2009, 10, 18, 12, 00, 00),
        )
    )
    .options(selectinload(Parent.children))
    .all()
)
assert parents[0] == p2
assert parents[0].children == [c5]
sess.expire_all()
# illustrate a 2.0 style query
print("------------------")
parents = (
    sess.execute(
        select(Parent)
        .execution_options(populate_existing=True)
        .options(
            temporal_range(
                range_lower=datetime.datetime(2009, 10, 15, 11, 00, 00),
                range_upper=datetime.datetime(2009, 10, 18, 12, 00, 00),
            )
        )
        .join(Parent.children)
        .filter(Child.id == 2)
    )
    .scalars()
    .all()
)
assert parents[0] == p1
print("-------------------")
assert parents[0].children == [c1, c2]
