from lib.send_text import *

class Confirm():

    def __init__(self, order, message_sender):
        self.order = order
        self.message_sender = message_sender

    def confirm_order(self):
        self.order.confirmed = True
        return self.message_sender.send_text_message()

    

