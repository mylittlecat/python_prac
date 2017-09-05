#!/usr/bin/env python
# -*- coding:utf-8 -*-
'makeTextFile.py --create text file'

import os
#ls is the symbol of line ending
ls=os.linesep

str=raw_input('Creat or Read a file?(c/r)\n')
if str=='c' or str=='C':	#不能简写成 str=='c' or 'C',这样写一直是True.   
    # get filename
    while True:
        fname=raw_input("Enter a filename: ")
        #check if the file already exist.
        if os.path.exists(fname):
            print "ERROR:'%s' already exists" % fname
        else:
            break

    # get file content(text)lines
    # creat an empty list
    all=[]
    print"\nEnter  lines('.' by iteself to quit).\n"

    # loop until user terminates input
    while True:
        entry=raw_input('Text input>:')
        if entry=='.':
            break
        else:
            # add a line to the list 
            all.append(entry)

    # write lines to file with proper line-ending
    fobj=open(fname,'w')
    fobj.writelines(['%s%s' % (x,ls) for x in all])
    fobj.close()
    print 'DONE!'

elif str=='r' or str=='R':

    'readTextFile.py -- read and display text file'

    # get filename
    fname=raw_input('Enter filename: ')
    print

    # attempt to open file for reading
    try:
        fobj=open(fname,'r')
    except IOError,e:
        print "*** file open error:",e
    else:
        # display contents to the screen
        for eachLine in fobj:
            eachLine=eachLine.rstrip()
            print eachLine
        fobj.close()
else:
    print 'quit process\n'
