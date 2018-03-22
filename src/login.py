"""
 * Created by PyCharm.
 * User: tuhoangbk
 * Date: 22/03/2018
 * Time: 15:46
 * Have a nice day　:*)　:*)
"""
from fbchat import Client
from fbchat.models import *

client = Client('tuhoang.bk2', 'hoanglung01')

print('Own id: {}'.format(client.uid))

client.send(Message(text='Hi me!'), thread_id=client.uid, thread_type=ThreadType.USER)

client.logout()