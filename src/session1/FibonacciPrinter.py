import os

class FibonacciPrinter:
    def __init__(self, totalRow, eachWidth):
        self.__totalRow = totalRow
        self.__eachWidth = eachWidth
    
    def getNum(self, row, column):
        if column == 1 or column == row or row == 1:
            return 1
        else:
            return self.getNum(row - 1, column - 1) + self.getNum(row - 1, column);
        
    def getLeftWidth(self, row, column):
        if self.__eachWidth / 2 != 0:
            raise Exception("each width variable should be even")
        rowStartDiff = self.__eachWidth / 2   
        return (self.__totalRow - row) * rowStartDiff + (column - 1) * self.__eachWidth
        
    def getNumLast(self, row):
        if row == 1:
            return 0
        elif row == 2:
            return 1
        else:
            return self.getNumLast(row - 1) + self.getNumLast(row - 2) 
    
    def getLeftWidthLast(self, row):
        rowStartDiff = self.__eachWidth / 2  
        return self.__totalRow * self.__eachWidth - (self.__totalRow - row) * rowStartDiff

    """
    This method only print the number and the following padding, do not print the padding prefix
    """
    def __getNumPrint(self , num):
        resultStr = str(num)
        for i in range(len(str(num)), self.__eachWidth):
            resultStr = resultStr + ' '
        return resultStr
     
    def __getNumPrintStr(self , row , column):
        num = self.getNum(row, column)
        return self.__getNumPrint(num)
     
        
    def getLinePrint(self , row):
        # First print the black characters     
        tmpStr = ''    
        for i in range(0, self.getLeftWidth(row, 1)):
            tmpStr = tmpStr + ' '
                
        for j in range(1, row + 1):
            tmpStr = tmpStr + self.__getNumPrintStr(row, j)
        
        # from here, start printing the last number
        lastNumFib = self.getNumLast(row)
        if lastNumFib != 0:
            tmpStr = tmpStr + self.__getNumPrint(lastNumFib)
        return tmpStr + os.linesep    

    def getAllLinesPrint(self):
        result = ''
        for i in range(0, self.__totalRow):
            result = result + str(self.getLinePrint(i + 1))
        return result
