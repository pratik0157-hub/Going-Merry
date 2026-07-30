#!/usr/bin/env python3
"""iterative"""
foo = [2, 4, 5, 7, 9, 10, 15, 20, 33, 59]
foo.sort()

n = int(input("Enter the number to search: "))

def binary_search(arr, x):
    low = 0 
    high = len(arr) - 1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid]<x:
            low = mid + 1
        else:
            return True

    return False

if binary_search(foo, n):
    print("found!!")
else:
    print("Not found!!")

"""recursive"""
foo = [2, 4, 5, 7, 9, 10, 15, 20, 33, 59]
foo.sort()

n = int(input("Enter the number to search: "))
start = 0
end = len(foo) - 1

def binary_search(arr, x, low, high):
    if low > high:
        return False
    mid = (low+high)//2
    if arr[mid] > x:
        return binary_search(arr,x,low,mid-1)
    elif arr[mid] < x:
        return binary_search(arr,x,mid +1, high)
    else:
        return True

if binary_search(foo, n, start, end):
    print("found!!")
else:
    print("Not found!!")