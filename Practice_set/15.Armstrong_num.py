#!/usr/bin/env python3

x = int(input("enter a number: "))
count = 0
for n in str(x):
    count +=1
total = 0
for w in str(x):
    num = int(w)
    total += num**count

if total == x:
    print("The given number is armstrong number.")
else:
    print("the given number is not armstong number.")
