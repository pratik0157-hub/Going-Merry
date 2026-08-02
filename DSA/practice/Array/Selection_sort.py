#!/usr/bin/env python3

foo = [10, 8, 4, 6, 5, 2, 9, 3]

def Selection_sort(arr):
    size = len(arr)
    for i in range(0, size):
        min_index = i
        for j in range(i+1, size):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]

    return arr

print(Selection_sort(foo))
