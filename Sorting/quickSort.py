#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Arif Khan
"""

def quickSort(myList):
    """ Quick sort implementation. """
    helper(myList, 0, len(myList) - 1)

def helper(myList, first, last):
    """ Helper function for quick sort."""
    if first < last:
        splitList = partitionList(myList, first, last)
        
        helper(myList, first, splitList - 1)
        helper(myList, splitList + 1, last)
    
    return myList
    
    
def partitionList(myList, first, last):
    """ Partitioning the list for sorting. """
    
    pivotValue = myList[first]
    leftMark = first + 1
    rightMark = last
    done = False
    
    while not done:
        while leftMark <= rightMark and myList[leftMark] <= pivotValue:
            leftMark += 1
        while rightMark >= leftMark and myList[rightMark] >= pivotValue:
            rightMark -= 1
        if rightMark < leftMark:
            done = True
        else:
            temp = myList[leftMark]
            myList[leftMark] = myList[rightMark]
            myList[rightMark] = temp
        
    temp = myList[first]
    myList[first] = myList[rightMark]
    myList[rightMark] = temp
    
    return rightMark



if __name__ == "__main__":
    
    print("=**********= Quick Sort =**********=")
    print()
    
    alist = [32,44,54,99,1,2,7,0,11,26,93,17,77,31,44,55,20]
    quickSort(alist)
    print(alist)