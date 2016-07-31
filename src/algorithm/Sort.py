'''
Merge sort
'''
from datetime import datetime
import random
from algorithm.heap import heap


def insert_sort(arr):
    result = [arr[0]]

    for i in range(1,len(arr)):
        val = arr[i]

        r_length = len(result)
        for j in range(r_length):
            if val>=result[j]:
                if(j==r_length-1):
                    result.append(val)
                    break
                else:
                    j += 1
            else:
                # part_move = result[j:]
                result.insert(j,val)
                break

    return result

def heap_sort(arr):
    h = heap(arr)
    for i in range(len(arr)-1, -1, -1):
        tmp = arr[0]
        arr[0] = arr[i]
        arr[i] = tmp

        h.max_heap(0)

    print h




def __swap(arr, p1, p2):
    if p1<0 or p1>len(arr)-1 or p2<0 or p2>len(arr)-1:
        return

    tmp = arr[p1]
    arr[p1] = arr[p2]
    arr[p2] = tmp


def quick_sort(arr, p, q):
    if p>=q:
        return

    pivlot, i,j= p, p+1 , q
    findLess = True
    while i<j:
        if findLess:
            if arr[i]<=arr[pivlot]:
                i += 1
            else:
                findLess = False
        else:
            if arr[pivlot] < arr[j]:
                j -= 1
            else:
                __swap(arr, i, j)
                findLess = True

    if arr[pivlot]<arr[i]:
        __swap(arr,pivlot,i-1)
        pivlot = i-1
    else:
        __swap(arr,pivlot,i)
        pivlot = i

    quick_sort(arr,p,pivlot-1)
    quick_sort(arr,pivlot+1,q)


def merge_sort(arr):
    n = len(arr)

    if(n==1):
        return arr
    else:
        firstPart =  merge_sort(arr[:n/2])
        secondpart = merge_sort(arr[(n/2):])

        return __merge_two(firstPart,secondpart)

def __merge_two(firstPart, secondpart):
    result = []
    i,j = 0 , 0
    len1 = len(firstPart)
    len2 = len(secondpart)
    while(i< len1 and j<len2):
        if(firstPart[i]<secondpart[j]):
            result.append(firstPart[i])
            i += 1
        else:
            result.append(secondpart[j])
            j += 1

    if i<len1:
        result.extend(firstPart[i:])
    if j<len2:
        result.extend(secondpart[j:])

    return result



def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list



if __name__ == '__main__':
    arr = random_int_list(1,100, 20)
    # arr = [8, 7, 3, 3, 7]
    # arr = [12, 84, 21, 68, 13, 81]
    should_print = True

    lenth = len(arr)
    # print arr[0:lenth/2]
    # print arr[lenth/2:lenth]

    print '================ merge sort starts================='
    if should_print:
        print "before merge sort :", arr

    t0 = datetime.now()
    print "@%s, {%s} start" % (t0, 'merge_sort')

    merge_sort(arr)

    t1 = datetime.now()
    print "@%s, {%s} end" % (t1, 'merge_sort')
    print "@%.3fs taken for {%s}" % ((t1-t0).seconds, 'merge_sort')



    print '================ quick sort starts================='
    if should_print:
        print "before quick sort :", arr
    t0 = datetime.now()
    print "@%s, {%s} start" % (t0, 'quick_sort')

    quick_sort(arr,0,len(arr)-1)

    t1 = datetime.now()
    print "@%s, {%s} end" % (t1, 'quick_sort')
    print "@%.3fs taken for {%s}" % ((t1-t0).seconds, 'quick_sort')

    if should_print:
        print "after quick sort :", arr


    print '================ heap sort starts================='
    if should_print:
        print "before heap sort :", arr
    t0 = datetime.now()
    print "@%s, {%s} start" % (t0, 'heap sort')

    heap_sort(arr)

    t1 = datetime.now()
    print "@%s, {%s} end" % (t1, 'heap sort')
    print "@%.3fs taken for {%s}" % ((t1-t0).seconds, 'heap sort')

    if should_print:
        print "after heap sort :", arr