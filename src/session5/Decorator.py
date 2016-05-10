'''
Created on 

@author: hadoop
'''
import time

def exeTime(func):  
    def newFunc(*args, **args2):
        print getattr(func,'__name__')  
        print id(func)
        t0 = time.time()  
        print "@%s, {%s} start" % (time.strftime("%X", time.localtime()), func.__name__)  
        back = func(*args, **args2)  
        print "@%s, {%s} end" % (time.strftime("%X", time.localtime()), func.__name__)  
        print "@%.3fs taken for {%s}" % (time.time() - t0, func.__name__)  
        return back  
    return newFunc 

@exeTime
def foo():  
    for i in xrange(100000):  
        pass  



if __name__ == '__main__':
    foo();
