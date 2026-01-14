from dataclasses import dataclass
import json
from sys import argv, exit, stderr


@dataclass
class Order:
    order_id: int
    from_location: str
    to_location: str
    is_taken: bool = False

    def __str__(self):
        return (
            f"{self.order_id},{self.from_location},{self.to_location},{self.is_taken}"
        )


orders: dict[int, Order] = {}


try:
    with open("data/orders.json", "r") as f:
        saved_orders = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    saved_orders = []

for order in saved_orders:
    orders[order["order_id"]] = Order(**order)


def create_order(from_location: str, to_location: str) -> int:
    if not from_location or not to_location:
        stderr.write("from and to locations are required")
        exit(1)

    order_id = max(orders.keys(), default=0) + 1
    new_order = Order(
        order_id=order_id, from_location=from_location, to_location=to_location
    )
    orders[order_id] = new_order
    with open("data/orders.json", "w") as f:
        json.dump([order.__dict__ for order in orders.values()], f)
    return order_id


def list_orders() -> list[Order]:
    return [order for order in orders.values() if not order.is_taken]


def take_order(order_id: int) -> Order:
    order = orders.get(order_id)
    if not order:
        stderr.write("order does not exist")
        exit(1)
    if order.is_taken:
        stderr.write("order already taken")
        exit(1)
    order.is_taken = True
    with open("data/orders.json", "w") as f:
        json.dump([order.__dict__ for order in orders.values()], f)
    return order


if __name__ == "__main__":
    if len(argv) < 2:
        stderr.write("you need to provide a command")
        exit(1)
    command = argv[1]
    if command == "create_order":
        if len(argv) < 4:
            stderr.write("you need to provide a from and to location")
            exit(1)
        from_location = argv[2]
        to_location = argv[3]
        order_id = create_order(from_location, to_location)
        print(order_id)

    elif command == "list_orders":
        orders = list_orders()
        for order in orders:
            print(f"{order.order_id},{order.from_location},{order.to_location}")

    elif command == "take_order":
        if len(argv) < 3:
            stderr.write("you need to provide an order id")
            exit(1)
        order_id = argv[2]
        if not order_id.isdigit():
            stderr.write("order id must be a number")
            exit(1)
        order = take_order(int(order_id))

    else:
        stderr.write("invalid command")
        exit(1)
