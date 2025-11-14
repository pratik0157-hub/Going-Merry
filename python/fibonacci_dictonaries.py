#!/usr/bin/env python3
def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans
def fib(n):
    d = {0: 0, 1: 1}
    return fib_efficient(n, d)
# Example usage:
