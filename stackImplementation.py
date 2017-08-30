#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Arif Khan
"""

class Stack:
    """ Stack class and it's functions """
    
    def __init__(self):
        """ Constructor for the stack class """
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        del(self.items[-1])
    def displayItems(self):
        for element in range(len(self.items) - 1, -1, -1):
            print(self.items[element])
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False


if __name__ == "__main__":
    
    myStack = Stack()
    
    menu = """
    1). Push
    2). Pop
    3). Display Items
    4). Quit
    """
    
    while True:
        print(menu)
        print()
        choice = int(input("Choice: "))
        if choice == 1:
            item = input("Enter Item: ")
            myStack.push(item)
        elif choice == 2:
            myStack.pop()
        elif choice == 3:
            if not myStack.isEmpty():
               myStack.displayItems()
            else:
               print("Stack is Empty")
        elif choice == 4:
            break