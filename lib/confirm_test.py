
from config import *
from order import *
from menu import *
from confirm import *

menu = Menu()
order = Order(menu)
item_one = MenuItem("Prawn Summer Rolls", 7.00 )
item_two = MenuItem("Tofu Summer Rolls", 7.00 )
order.add(item_one)
order.add(item_two)

confirm = Confirm(order)
confirm.confirm_order()