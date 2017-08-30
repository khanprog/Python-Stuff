# -*- coding: utf-8 -*-
"""
@author: Arif Khan
"""

def insertionSort(myList):
    """ Insertion sort algorithm implementation."""
    for item in range(1, len(myList)):
        
        currentValue = myList[item]
        position = item
        
        while myList[position - 1] > currentValue and position > 0:
            myList[position] = myList[position - 1]
            position -= 1
        myList[position] = currentValue
    return myList


if __name__ == "__main__":
    
    print("=**********= Insertion Sort =**********=")
    print()
    
    alist = [32,44,54,99,1,2,7,0,11,26,93,17,77,31,44,55,20]
    
    print(insertionSort(alist))