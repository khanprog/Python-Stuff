# -*- coding: utf-8 -*-
"""
@author: Arif Khan
"""

"""
pseudocode

1.  Found <- False
2.  while not Found and first <= top
3.  Midpoint <- (First + Last) DIV 2
4.  If List[Midpoint] = ItemSought Then
5.  ItemFound <- True
6.  Else
7.  If First >= Last Then
8.  SearchFailed <- True
9.  Else
10. If List[Midpoint] > ItemSought Then
11. Last <- Midpoint - 1
12. Else
13. First <- Midpoint + 1
14. EndIf
15. EndIf
16. EndIf

"""

def binarySearch(item, myList):
    
    found = False
    bottom = 0
    top = len(myList) - 1
    
    while not found and bottom <= top:
        
        midpoint = (bottom + top) // 2
        
        if myList[midpoint] == item:
            found = True
        elif myList[midpoint] < item:
            bottom = midpoint + 1
        else:
            top = midpoint - 1
    return found


if __name__ == "__main__":
    
    print("=**********= Binary Search =**********=")
    
    mylist = [1,2, 5, 7, 12, 14, 21, 28, 31, 36]
    
    search = int(input("Input the Item: "))
    
    isFound = binarySearch(search, mylist)
    
    print()
        
    if isFound:
        print("The '{}' is in the list.".format(search))
    else:
        print("The '{}' is not in the list.".format(search))
        
    
    