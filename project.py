import sys

def function1():
    print("hello i am first.")

def funtion2():
    print("hello i am second.")

arguments = sys.argv[1:]
if len(arguments) != 1:
    print("error")
