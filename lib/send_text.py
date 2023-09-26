from lib.config import *
from twilio.rest import Client

class SendText():

    def __init__(self, message):
        self.message = message

    def send_text_message(self):

        acc_sid = account_sid 
        token = auth_token
        client = Client(acc_sid, token)

        message = client.messages.create(
        from_=from_num,
        body=self.message,
        to=to_num
        )

        print(message.sid)
        return self.message
    
