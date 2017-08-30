# -*- coding: utf-8 -*-
"""
@author: Arif Khan
"""
"""
Repeat
    X ← StartofArray
    Flag ← False
    Repeat
        If Number(X) > Number (X+ 1) Then
            Temp ← Number(X)
            Number (X) ← Number (X+ 1)
            Number(X+I) ← Temp
            Flag ← True
        End If
        X ← X+1
    Until EndofArray
Until Flag = False

"""

def bubbleSort(myList):
    """ Bubble sort algorithm implementation."""
    flag = True
    
    while flag:
        flag = False
        for item in range(len(myList) - 1):
            if myList[item] > myList[item + 1]:
                flag = True
                temp = myList[item]
                myList[item] = myList[item + 1]
                myList[item + 1] = temp
    return myList


if __name__ == "__main__":
    print("=**********= Bubble Sort =**********=")
    print()
    List = [1,12, 5, 7, 18, 11, 6, 12, 4, 17, 1]
    print(bubbleSort(List))