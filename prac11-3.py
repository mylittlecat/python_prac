#!/usr/bin/env python

def max2(a,b):
    'get the bigger one'
    if a>b:
        return a
    else:
        return b
def min2(a,b):
    'get the smaller one'
    if a<b:
        return a
    else:
        return b

def max(*args):
    max=args[0]
    for i in args:
        max=max2(max,i)
    return max
def min(*args):
    min=args[0]
    for i in args:
        min=min2(min,i)
    return min
print max(1,2,3,4,5,6,8,76,32,543765,432,231353)
print min(1,2,3,4,5,6,8,76,32,543765,432,231353)
