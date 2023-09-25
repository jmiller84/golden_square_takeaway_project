from lib.menu import *


"""
initialise a menu object and check it has 3 starters
"""
def test_menu_has_three_starters():
    menu = Menu()
    assert len(menu.starters) == 3


"""
initialise a menu object and check it has 3 mains
"""
def test_menu_has_three_mains():
    menu = Menu()
    assert len(menu.mains) == 3



"""
initialise a menu object and check it has 3 desserts
"""
def test_menu_has_three_desserts():
    menu = Menu()
    assert len(menu.desserts) == 3




