
from config import *
from twilio.rest import Client
from order import *
from menu import *


class Confirm():

    def __init__(self, order):
        self.order = order

    def confirm_order(self):
        # sets self.order.confirmed to True 
        # sends text message to user
        self.order.confirmed = True

        account_sid = 'AC7f4404071dc0638248dbce740e6328c8'
        token = auth_token
        client = Client(account_sid, token)

        message = client.messages.create(
        from_='+447723918953',
        body='Thank you! Your order was placed and will be delivered before 18:52',
        to='+447877155379'
        )

        print(message.sid)
        
