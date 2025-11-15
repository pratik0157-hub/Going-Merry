#!/usr/bin/env python3

for n in range(2, 11):
    for w in range(2, int(n/2)):
        if n % w == 0:
            continue
        else:
            print(n)

