from lib.menu_item import *

class Menu():

    def __init__(self):


        self.starters = [
            MenuItem("Prawn Summer Rolls", 7.00 ),
            MenuItem("Tofu Summer Rolls", 7.00 ),
            MenuItem("Veg Spring Rolls", 7.00 ),
        ]

        self.mains = [
            MenuItem("Chicken Pho", 11.00 ),
            MenuItem("Beef Pho", 11.00 ),
            MenuItem("Tofu Pho", 11.00 ),
        ]

        self.desserts = [
            MenuItem("Ice Cream", 5.00 ),
            MenuItem("Chocolate Brownie", 5.00 ),
            MenuItem("Banana Fritters", 5.00 ),
        ]


    def display_menu(self):
    
        print("""
              STARTERS
              """)
   
        for item in self.starters:
            print(f"{item.name}, £{item.price}")

        print("""
              MAINS
              """)
        
        for item in self.mains:
            print(f"{item.name}, £{item.price}")

        print("""
              DESSERTS
              """)
        
        for item in self.desserts:
            print(f"{item.name}, £{item.price}")
    



# menu = Menu()
# menu.display_menu()