"""
 * Created by PyCharm.
 * User: tuhoangbk
 * Date: 22/03/2018
 * Time: 15:52
 * Have a nice day　:*)　:*)
"""
import pickle
from os.path import join
class Account():
    def __init__(self):
        pass
    
    def save_obj(self, obj, name ):
        with open(join('../pickle', name), 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
    
    def load_obj(self, name ):
        with open(join('../pickle', name), 'rb') as f:
            return pickle.load(f)

if __name__ == "__main__":
    tuhoangbk2 = Account()
    acc_clone = {'usr':'tuhoang.bk2', 'pas':'hoanglung01'}
    acc_clone2 = {'usr':'100025070615763', 'pas':'hoanglung01'}
    tuhoangbk2.save_obj(acc_clone, 'tuhoang_clone.pkl')
    tuhoangbk2.save_obj(acc_clone2, 'tuhoang_clone2.pkl')
    print('ahii')