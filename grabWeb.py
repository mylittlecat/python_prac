#!/usr/bin/env python

from urllib import urlretrieve
def firstNonBlank(lines):
    for eachLine in lines:
        if not eachLine.strip():
            continue
        else:
            return eachLine

def firstLast(webpage):
    f=open(webpage)
    if not f:
        print 'yes!'
    lines=f.readlines()
    f.close()
    print firstNonBlank(lines),
    lines.reverse()
    print firstNonBlank(lines),
def download(url='https://www.baidu.com',process=firstLast):
    try:
        retval=urlretrieve(url)[0]
    except IOError:
        retval=None
    if retval: # do some processing
        process(retval)
    else:
        print'retval is None!\n'
if __name__=='__main__':
    download('http://www.hust.edu.cn')
