from lib.menu_item import *

"""
Create a new menu item and check it has a name
"""
def test_new_menu_item_has_name():
    item = MenuItem("Prawn Summer Rolls", 7.00)
    assert item.name == "Prawn Summer Rolls"


"""
Create a new menu item and check it has a price
"""
def test_new_menu_item_has_price():
    item = MenuItem("Prawn Summer Rolls", 7.00)
    assert item.price == 7.00