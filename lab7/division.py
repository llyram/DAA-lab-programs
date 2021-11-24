#!/bin/python

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of a: "))

try:
    print("value of a/b = " + str(a/b))
except ZeroDivisionError:
    print("Exception! Division by 0 is not permitted!")
