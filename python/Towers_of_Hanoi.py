#!/usr/bin/env python3
def printMover(fr, to):
    print("Move disk from rod", str(fr), "to rod", str(to))
def Towers(n, fr, to, spare):
    if n == 1:
        printMover(fr, to)
    else:
        Towers(n - 1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n - 1, spare, to, fr)
