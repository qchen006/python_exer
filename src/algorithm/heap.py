class heap:
    def __init__(self, arr):
        self.__data = arr

        length = len(arr)
        for i in range(length-1 , -1 , -1):
            self.max_heap(i)

    def max_heap(self, i):
        left_val = self.__left_val(i)
        right_val = self.__right_val(i)

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
            else:
                self.__data[2 * i + 2] = tmp

    def __left_val(self, i):
        if (2 * i + 1 < len(self.__data)):
            return self.__data[2 * i + 1]
        else:
            return None

    def __right_val(self, i):
        if (2 * i + 2 < len(self.__data)):
            return self.__data[2 * i + 2]
        else:
            return None

    def __str__(self):
        result = ''
        for i in range(len(self.__data)):
            result = result + ' ' + str(self.__data[i])
        return result


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    h = heap(arr)
    # h._max_heap(0)
    print h
