

class Order():

    def __init__(self, menu):
        self.menu = menu
        self.order_list = []
        self.confirmed = False

    def add(self, menu_item):
        self.order_list.append(menu_item)

    def remove(self, menu_item):
        self.order_list.remove(menu_item)


