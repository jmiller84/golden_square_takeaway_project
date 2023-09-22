from lib.order import *
from lib.menu import *
from lib.menu_item import *

"""
Create new order and check it returns an empty list
"""
def test_new_order_has_empty_list():
    menu = Menu()
    order = Order(menu)
    assert order.order_list == []

"""
Create new order and check that confirmed attributre is set to False
"""
def test_new_order_is_not_confirmed():
    menu = Menu()
    order = Order(menu)
    assert order.confirmed == False

"""
Create new order and add 2 items to order
"""
def test_add_two_menu_items():
    menu = Menu()
    order = Order(menu)
    item_one = MenuItem("Prawn Summer Rolls", 7.00 )
    item_two = MenuItem("Tofu Summer Rolls", 7.00 )
    order.add(item_one)
    order.add(item_two)
    assert order.order_list == [item_one, item_two]


"""
Add 2 items to order and remove one item
"""
def test_remove_one_item_from_order():
    menu = Menu()
    order = Order(menu)
    item_one = MenuItem("Prawn Summer Rolls", 7.00 )
    item_two = MenuItem("Tofu Summer Rolls", 7.00 )
    order.add(item_one)
    order.add(item_two)
    order.remove(item_two)
    assert order.order_list == [item_one]


