#!/usr/bin/env python3

foo = [10, 4, 14, 7, 3, 9]

def partition(arr):
    size = len(arr)

    key = arr[size - 1]
    temp = [0]*size
    i = 0

    for j in range(0, size):
        if key >= arr[j]:
            temp[i] = arr[j]
            i += 1

    for j in range(0, size):
        if key < arr[j]:
            temp[i] = arr[j]
            i += 1

    for n in range(0, size):
        arr[n] = temp[n]

print(foo)
partition(foo)
print(foo)