#!/usr/bin/env python

'makeTextFile.py --create text file'

import os
#ls is the symbol of line ending
ls=os.linesep

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
