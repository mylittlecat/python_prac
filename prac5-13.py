#!/usr/bin/env python

def TimeTrans():
    'transform time into minutes'
    a=raw_input("Enter a time: ")
    aList=a.split(':')
    return int(aList[0])*60+int(aList[1])
print TimeTrans()
