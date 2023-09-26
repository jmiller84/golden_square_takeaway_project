from lib.order import *
from lib.menu import *
from lib.menu_item import *
from lib.confirm import *

from unittest.mock import Mock


"""
Test confirm order sets the order status to complete
"""
def test_mock_order_status_is_complete():
    order = Mock()
    message_sender = Mock()
    confirm = Confirm(order, message_sender)
    message_sender.send_text_message.return_value = "Thank you! Your order was placed and will be delivered before 18:52"
    confirm.order.confirmed = True
    assert confirm.confirm_order() == "Thank you! Your order was placed and will be delivered before 18:52"
    assert confirm.order.confirmed == True


