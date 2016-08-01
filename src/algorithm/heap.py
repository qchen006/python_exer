import math
import os


class heap:
    def __init__(self, arr):
        self.__data = arr

        self.unit_width = 2

        height = 1
        while math.pow(2,height) - 1<len(self.__data):
            height += 1
        self.__height = height

        length = len(arr)
        for i in range(int(math.pow(2, self.__height-1))-1 , -1 , -1):
            self.max_heap(i, len(self.__data) -1)


    def max_heap(self, i, maximum):
        if maximum == -1:
            maximum = len(self.__data) -1

        if maximum < 2*i+1:
            return

        left_val = self.__left_val(i ,maximum)
        right_val = self.__right_val(i, maximum)

        if left_val is None:
            return

        '''
        bigger_left tuple stores the bigger value and boolean whether the bigger value is left child
        '''

        if right_val is None:
            bigger_left = (left_val, True)
        else:
            bigger_left = (left_val, True) if left_val > right_val else (right_val, False)

        if bigger_left[0] > self.__data[i]:
            tmp = self.__data[i]
            self.__data[i] = bigger_left[0]

            if bigger_left[1]:
                self.__data[2 * i + 1] = tmp
                self.max_heap(2*i +1, maximum)
            else:
                self.__data[2 * i + 2] = tmp
                self.max_heap(2*i +2, maximum)



    def __left_val(self, i, maximum):

        if (2 * i + 1 <= maximum):
            return self.__data[2 * i + 1]
        else:
            return None

    def __right_val(self, i ,maximum):

        if (2 * i + 2 <= maximum):
            return self.__data[2 * i + 2]
        else:
            return None

    def __str__(self):
        result = ''
        for i in range(1, self.__height+1):
            result = result + ' ' + self.getLinePrint(i)
        return result

    def getLinePrint(self , row):
        # First print the black characters
        tmpStr = ''
        if row != self.__height:
            for i in range(0, self.getRowUnitWidth(row)):
                tmpStr = tmpStr + ' '

        for j in range(1, int(math.pow(2,row-1))+1):
            i = int(math.pow(2, row-1)) + j - 2
            if(i<len(self.__data)):
                sep = ' '
                for j in range(0, self.getRowUnitWidth(row)):
                    sep = sep + ' '
                tmpStr = tmpStr + str(self.__data[i]) +sep
            else:
                break

        return tmpStr + os.linesep


    def getRowUnitWidth(self, row):
        # if self.__eachWidth / 2 != 0:
        #     raise Exception("each width variable should be even")
        rowStartDiff = self.unit_width * (int(math.pow(2,self.__height -1))+1) / row
        return rowStartDiff


if __name__ == '__main__':
    # arr = [1, 2, 3, 4,5,6,7, 8,2,19,32,8 , 1, 2, 3]
    arr = [12, 42, 48, 51, 55, 82]
    h = heap(arr)
    # h._max_heap(0)
    print h
