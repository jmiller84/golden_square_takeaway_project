from lib.order import *
from lib.menu import *
from lib.menu_item import *
from lib.display_order import *
from unittest.mock import Mock

"""
Create new order using a mock menu and check it returns an empty list
"""
def test_new_order_has_empty_list_for_mock_menu():
    mock_menu = Mock()
    mock_menu.order_list = []
    order = Order(mock_menu)
    assert order.order_list == []



"""
Create new order with mock menu and check that confirmed attributre is set to False
"""
def test_new_order_for_mock_menu_is_not_confirmed():
    mock_menu = Mock()
    order = Order(mock_menu)
    assert order.confirmed == False


"""
Create new order and add 2 items to order
"""
def test_add_two_mock_menu_items():
    mock_menu = Mock()
    order = Order(mock_menu)
    item_one_mock = Mock()
    item_two_mock = Mock()
    order.add(item_one_mock)
    order.add(item_two_mock)
    assert order.order_list == [item_one_mock, item_two_mock]


"""
Add 2 items to order and remove one item
"""
def test_remove_one_mock_item_from_order():
    mock_menu = Mock()
    order = Order(mock_menu)
    item_one_mock = Mock()
    item_two_mock = Mock()
    order.add(item_one_mock)
    order.add(item_two_mock)
    order.remove(item_two_mock)
    assert order.order_list == [item_one_mock]


