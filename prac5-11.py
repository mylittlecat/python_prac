#!/usr/bin/env python

def even():
    'get evens in 0~20'
    return [i for i in range(21) if not i%2]
def odd():
    'get evens in 0~20'
    return [i for i in range(21) if i%2]
print even()
print odd()
print 'Enter two numbers: '
a=int(raw_input(">"))
b=int(raw_input(">"))
if not a%b or not b%a:
    print "True"
else:
    print "False"

