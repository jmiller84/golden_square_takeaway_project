from lib.order import *

class DisplayOrder():

    def __init__(self, order):
        self.order = order
  

    def display_order(self):

        total = sum([item.price for item in self.order.order_list])

        for item in self.order.order_list:
            print(f"{item.name}, £{item.price}")

        print(f"Total = £{total}")
        return total 

# from menu import *
# menu = Menu()
# order = Order(menu)
# item_one = MenuItem("Prawn Summer Rolls", 7.00 )
# item_two = MenuItem("Tofu Summer Rolls", 7.00 )
# order.add(item_one)
# order.add(item_two)
# display = DisplayOrder(order)

# display.display_order()

