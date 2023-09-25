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


