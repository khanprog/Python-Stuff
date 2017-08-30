# -*- coding: utf-8 -*-
"""
@author: Arif Khan

pseudocode

1. position <- 0
2. found <- False
3. while position < len(List) and not found:
4. if List[position] = item:
5. found <- True
6. position <- position + 1
    
"""


def linearSearch(item, myList):
    """ Algorithm Implementation """
    position = 0
    found = False
    while position < len(myList) and not found:
        if myList[position] == item:
            found = True
        position += 1
    return found



if __name__ == "__main__":
    
    print("=**********= Linear Search =**********=")
    
    mylist = []
    
    while True:
        item = input("Input item to add to the list(hit return to finish): ")
        if item == "":
            break
        else:
            mylist.append(item)
    
    search = input("Input the item to search for: ")
    
    print()
    
    found = linearSearch(search, mylist)
    
    if found:
        print("The '{}' is in the list.".format(search))
    else:
        print("The '{}' is not in the list.".format(search))
        
    
    