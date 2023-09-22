from lib.display_order import *
from lib.menu import *
from lib.order import *


"""
Return the total cost of the order
"""
def test_returns_total_cost():
    menu = Menu()
    order = Order(menu)
    item_one = MenuItem("Prawn Summer Rolls", 7.00 )
    item_two = MenuItem("Tofu Summer Rolls", 7.00 )
    order.add(item_one)
    order.add(item_two)
    display = DisplayOrder(order)

    assert display.display_order() == 14.00