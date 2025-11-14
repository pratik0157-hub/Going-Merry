#!/usr/bin/env python3
def getData(data):
    nums = ()
    words = ()
    for t in data:
        nums += (t[0],)
        if t[1] not in words:
            words += (t[1],)
    return (min(nums), max(nums), len(words))
