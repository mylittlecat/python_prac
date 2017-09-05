#!/usr/bin/env python

'readTextFile.py -- read and display text file'

import os

# get filename
fname=raw_input('Enter filename: ')
print 

# attempt to open file for reading
if not os.path.exists(fname):
    print 'file open error'
else:
    # display contents to the screen
    fobj=open(fname,'r')
    for eachLine in fobj:
        print eachLine,
    fobj.close()
