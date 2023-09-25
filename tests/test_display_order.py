from lib.display_order import *
from lib.menu import *
from lib.order import *
from unittest.mock import Mock
from unittest.mock import patch, call


"""
Add mock items and return the total cost of the order
"""
def test_add_mock_items_and_return_total_cost():
    mock_menu = Mock()
    order = Order(mock_menu)
    item_one_mock = Mock()
    item_two_mock = Mock()
    item_one_mock.name = "Prawn Summer Rolls"
    item_one_mock.price = 7.00
    item_two_mock.name = "Tofu Summer Rolls"
    item_two_mock.price = 7.00
    order.add(item_one_mock)
    order.add(item_two_mock)
    display = DisplayOrder(order)

    assert display.display_order() == 14.00


