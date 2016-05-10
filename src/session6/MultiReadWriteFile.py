'''

@author: hadoop
'''
from session6.FileReader import FileReader
from session6.FileWriter import FileWriter

if __name__ == '__main__':
    numWriter = 2
    numReader = 1
    for i in range(0, numWriter):
        writer=FileWriter('data',i)
        writer.start()
    
    for i in range(0, numReader):
        reader=FileReader('data')
        reader.start() 
  