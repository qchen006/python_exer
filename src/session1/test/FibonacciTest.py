'''
Created on 2016/04/02

@author: hadoop
'''
import unittest
from session1 import FibonacciPrinter
from session1.FibonacciPrinter import FibonacciPrinter

totalRow = 4
eachWidth = 2
fibonacciPrinter = FibonacciPrinter(totalRow, eachWidth)

class Test(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass


    def testGetNum(self):
        self.assertEqual(fibonacciPrinter.getNum(1, 1), 1, "Fail for getNum(2,2)")
        self.assertEqual(fibonacciPrinter.getNum(2, 2), 1, "Fail for getNum(1,1)")
        self.assertEqual(fibonacciPrinter.getNum(5, 4), 4, "Fail for getNum")
        
    def testGetLeftWidth(self):
#         self.assertEqual(fibonacciPrinter.getLeftWidth(totalRow, 1), 0, "")
#         self.assertEqual(fibonacciPrinter.getLeftWidth(totalRow-1, 1),eachWidth/2, "")
        
        # This following test depends on the total row and width   
        self.assertEqual(fibonacciPrinter.getLeftWidth(2, 2), 4, "")  
        
    def testGetNumLast(self):
        self.assertEqual(fibonacciPrinter.getNumLast(1), 0, "")
        self.assertEqual(fibonacciPrinter.getNumLast(2), 1, "")
        self.assertEqual(fibonacciPrinter.getNumLast(3), 1, "")
        self.assertEqual(fibonacciPrinter.getNumLast(4), 2, "")
        self.assertEqual(fibonacciPrinter.getNumLast(8), 13, "")
        
    def testGetLeftWidthLast(self):
        self.assertEqual(fibonacciPrinter.getLeftWidthLast(1), 5, "")
        self.assertEqual(fibonacciPrinter.getLeftWidthLast(2), 6, "")
        self.assertEqual(fibonacciPrinter.getLeftWidthLast(3), 7, "")

    def testPrintNum(self):
        print(fibonacciPrinter.getLinePrint(1))
        print(fibonacciPrinter.getAllLinesPrint())                            
        
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testGetNum']
    #
#         print getLeftWidth(1, 1)
#         print getLeftWidth(1, 1)
        
#         print getNumLast(5)
    unittest.main()
