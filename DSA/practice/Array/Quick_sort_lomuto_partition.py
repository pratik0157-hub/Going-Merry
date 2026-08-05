#!/usr/bin/env python3


foo = [10, 4, 14, 7, 3, 9, 21]
"""this isn't the original one its a variant one """
def partition(arr, low, high):
    key = arr[high]
    """i is the wall and j is the index"""
    i = low - 1
    for j in range(low,high):
        if key > arr[j]:
            i += 1
            swap(arr, i, j)
    swap(arr, i+1, high)
    return i+1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def Quick_sort(arr, low, high):

    if low < high:
        pi = partition(arr, low ,high)

        Quick_sort(arr, low, pi - 1)
        Quick_sort(arr , pi +1 , high)
print(foo)
Quick_sort(foo, 0, 6)
print(foo)
