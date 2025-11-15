#!/usr/bin/env python3

x = int(input("enter any number: "))
for n in range(2, int(x/2)):
    if x % n == 0:
        prime = 0
        break
    else:
        prime = 1

if prime == 0:
    print("Number is not prime.")
else:
    print("Number is prime")
