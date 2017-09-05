#!/usr/bin/env python

from random import randint

def CreatTime():
    'creat a time in minutes'
    a=randint(0,24*60)
    print a
    if a%60 <10:
        stdtime=str(a/60)+':'+'0'+str(a%60)
    else:
        stdtime=str(a/60)+':'+str(a%60)
    return stdtime
def TimeTrans():
    'transform time into minutes'
    a=raw_input("Enter a time: ")
    aList=a.split(':')
    return int(aList[0])*60+int(aList[1])
print CreatTime()
print TimeTrans()
