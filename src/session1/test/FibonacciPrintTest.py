'''
Created on 2016/04/02

@author: hadoop
'''
import unittest
from session1 import FibonacciPrinter
from session1.FibonacciPrinter import FibonacciPrinter

totalRow = 17
eachWidth = 8
fibonacciPrinter = FibonacciPrinter(totalRow, eachWidth)

class Test(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def testPrintNum(self):
        print fibonacciPrinter.getAllLinesPrint()                            
        
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testGetNum']
    #
#         print getLeftWidth(1, 1)
#         print getLeftWidth(1, 1)
        
#         print getNumLast(5)
    unittest.main()
