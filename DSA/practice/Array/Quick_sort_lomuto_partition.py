#!/usr/bin/env python3


foo = [10, 4, 14, 7, 3, 9, 21]
"""this isn't the original one its a variant one """
def Quick_sort_lomoto(arr, low, high):
    size = len(arr)
    key = arr(size - 1)
    """i is the wall and j is the index"""
    i = 0
    for j in range(0,size-1):
        if key > arr[j]:
            dummy = arr[j]
            arr[j] = arr[i]
            arr[i] = dummy
            i += 1
    arr[size - 1] = arr[i]
    arr[i] = key
