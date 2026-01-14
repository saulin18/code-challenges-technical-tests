from src.main import Order, create_order, list_orders, take_order, orders
import json
import pytest


@pytest.fixture(autouse=True)
def reset_orders():
    with open("data/orders.json", "w") as f:
        orders.clear()
        json.dump([], f)
       
        

def test_create_order():
    order_id = create_order("Mong Kok", "Central")
    assert order_id == 1
    with open("data/orders.json", "r") as f:
        orders: list[dict] = json.load(f)
    assert len(orders) == 1


def test_list_orders():
    orders = list_orders()
    assert len(orders) == 0
    create_order("Mong Kok", "Central")
    orders = list_orders()
    assert len(orders) == 1
    assert orders[0].order_id == 1
    assert orders[0].from_location == "Mong Kok"
    assert orders[0].to_location == "Central"
    assert not orders[0].is_taken


def test_take_order():
    order_id = create_order("Mong Kok", "Central")
    order = take_order(order_id)
    assert order.order_id == order_id
    assert order.from_location == "Mong Kok"
    assert order.to_location == "Central"
    assert order.is_taken


def test_take_order_already_taken():
    order_id = create_order("Mong Kok", "Central")
    order = take_order(order_id)
    with pytest.raises(SystemExit):
        take_order(order_id)
    assert order.is_taken


def test_taken_orders_not_appearing_in_list_orders():
    order_id = create_order("Mong Kok", "Central")
    take_order(order_id)
    orders = list_orders()
    assert len(orders) == 0
