#!/usr/bin/env python3
l = [2, 4, 7]
r = [3, 5, 9, 10]
foo = [3, 2, 4, 6, 8, 10, 23]

def merge(left, right):
     size = len(left)+len(right)
     arr = [0]* size
     k = 0
     i = 0
     j = 0
     while i < len(left) and j<len(right):
          if left[i]>=right[j]:
               arr[k] = right[j]
               j+=1
               k +=1
          else:
               arr[k] = left[i]
               i +=1
               k+=1
     while i < len(left):
          arr[k] = left[i]
          i+=1
          k+=1
     while j < len(right):
          arr[k]= right[j]
          j+=1
          k+=1
     return arr

def Merge_sort(arr):
     size = len(arr)
     mid = size // 2
     if len(arr) != 1:
          left = Merge_sort(arr[0: mid])
          right = Merge_sort(arr[mid: size])
          return merge(left, right)
     else:
          return arr 

print(Merge_sort(foo))  