'''
Created on 2016/04/02

@author: hadoop
'''
import sys
import os
from session1.FibonacciPrinter import FibonacciPrinter
from session1 import LovePrinter


if __name__ == '__main__':
    
    prompt = "Please input:" +os.linesep
    prompt = prompt+"1: Print Fibo"+os.linesep
    prompt = prompt +"2: Print Love"+os.linesep
    prompt = prompt +"3: Exit"+os.linesep
    
    while True:
        x = raw_input(prompt)   #raw_inut reads as string, while input() reads as integer
        if x=='1':
            fPrint = FibonacciPrinter(17,8)
            print fPrint.getAllLinesPrint()
        elif x=='2':
            LovePrinter.printLove()
        elif x=='3':
            print "Exiting system"
            sys.exit()
        else:
            print "Please input 1 , 2 or 3"