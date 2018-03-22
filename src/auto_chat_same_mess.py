"""
 * Created by PyCharm.
 * User: tuhoangbk
 * Date: 22/03/2018
 * Time: 15:49
 * Have a nice day　:*)　:*)
"""

from fbchat import log, Client
from account import Account
from fbchat.models import *
import time

# Subclass fbchat.Client and override required methods
class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)
        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
        # If you're not the author, echo
        if author_id != self.uid:
            self.send(Message(text='Tú đang bận, vui lòng để lại tin nhắn sau tiếng Bíp'), author_id, thread_type=ThreadType.USER)
            time.sleep(5)
            self.send(Message(text='Beep!! :poop: :poop: :poop: :poop: :poop: :poop:'), author_id, thread_type=ThreadType.USER)
            # self.send(message_object, thread_id=thread_id, thread_type=thread_type)

account = Account()
xx = account.load_obj('tuhoang_clone.pkl')
client = EchoBot(xx['usr'], xx['pas'])
client.listen()
