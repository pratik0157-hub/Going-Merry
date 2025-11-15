#!/usr/bin/env python3

x = int(input("Enter the number: "))
factorial = 1
for n in range(1, x+1):
    factorial *= n

print("Factorial of the given number: ", factorial)