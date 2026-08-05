#!/usr/bin/env python3

foo = [5, 3, 8, 4, 2, 7, 1, 10]

def partition(arr):
    i = -1
    j = len(arr)
    key = arr[0]

    while True:
        while True:
            i += 1
            if key <= arr[i]:
                break

        while True:
            j -= 1
            if key >= arr[j]:
                break
        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i]
print(foo)
partition(foo)
print(foo)
