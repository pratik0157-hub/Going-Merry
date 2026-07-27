#!/usr/bin/env python3

"""Iterative Approach"""
# Iterate Python Program to print alternate elements
# of the array

def getAlternates(arr):
    final = []
    
    # Iterate over all alternate elements
    for i in range(0, len(arr), 2):
        final.append(arr[i])
    return final

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    res = getAlternates(arr)
    print(" ".join(map(str, res)))