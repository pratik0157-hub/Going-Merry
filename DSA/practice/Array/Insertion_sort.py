#!/usr/bin/env python3

foo = [10, 4, 14, 7, 3, 9, 21]

def Insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

print(Insertion_sort(foo))