'''
Created on 2016/04/02

@author: hadoop
'''
##  blank  blank *  blank * t/f
import os

def printLove():
    arraylist = [
         [2 ,4 ,3 ,8 ,0 ,0 ],
         [2 ,1 ,9 ,5 ,0 ,0 ],
         [2 ,0 ,12,3 ,0 ,0 ],
         [2 ,0 ,13,2 ,0 ,0 ],
         [2 ,0 ,15,0 ,0 ,0 ],
         [2 ,1 ,7 ,4 ,3 ,0 ],
         [2 ,2 ,6 ,5 ,2 ,1 ],
         [2 ,3 ,6 ,5 ,1 ,1 ],
         [2 ,5 ,6 ,4 ,0 ,1 ],
         [2 ,8 ,6 ,1 ,0 ,1 ],
         [2 ,10,5 ,0 ,0 ,1 ],
         [2 ,11,4 ,0 ,0 ,1 ],
         [2 ,12,3 ,0 ,0 ,1 ],
         [2 ,13,2 ,0 ,0 ,1 ],
         [2 ,15,0 ,0 ,0 ,1 ]
         ]
    
    tmp=""
    for i in range(0, 15):
        for j in range(0 , arraylist[i][0]):
            tmp=tmp+' '
        for k in range(1, 5):
                for l in range(0, arraylist[i][k]):
                    if k%2!=0:
                        tmp=tmp+' '
                    else:
                        tmp=tmp+'*'
                        
        for m in range(5, 6):
                    if arraylist[i][m] ==1: 
                        tmp=tmp+'*'
                    else:
                        tmp=tmp+' '
        
        for k in range(1, 5):
                for l in range(0, arraylist[i][5-k]):
                    if (5-k)%2!=0:
                        tmp=tmp+' '
                    else:
                        tmp=tmp+'*'
        
        for j in range(0 , arraylist[i][0]):
            tmp=tmp+' '
        
        tmp=tmp+os.linesep
        
    print tmp

