'''
Created on 

@author: hadoop
'''
from datetime import datetime
import time

def exeTime(func):
    def newFunc(*args, **args2):
        print getattr(func,'__name__')  
        print id(func)
        t0 = time.time()  
        print "@%s, {%s} start" % (datetime.now(), func.__name__)
        back = func(*args, **args2)  
        print "@%s, {%s} end" % (datetime.now(), func.__name__)
        print "@%.3fs taken for {%s}" % (time.time() - t0, func.__name__)  
        return back  
    return newFunc 

@exeTime
def foo():  
    for i in xrange(1000000):

        pass  



if __name__ == '__main__':
    foo();
