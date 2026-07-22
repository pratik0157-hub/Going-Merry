#!/usr/bin/env python3
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def square_root(num):
    if num <0:
        return None
    if num==0:
        return 0
    x = num
    eps = 1e-6
    while abs(x*x - num)>eps:
        x=(x + num/x)/2
    return x

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    

def printMover(fr, to):
    print("Move disk from rod", str(fr), "to rod", str(to))
def Towers(n, fr, to, spare):
    if n == 1:
        printMover(fr, to)
    else:
        Towers(n - 1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n - 1, spare, to, fr)
