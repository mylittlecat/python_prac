#!/usr/bin/env python
# coding:utf-8
# 用于下载192.168.80.3服务器文件的小程序

import ftplib
import os
import socket

HOST = '192.168.80.3'
DIRN = '/home/acorn'
FILE = 'db_test1.py'

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror), e:
        print 'ERROR: cannot reach "%s"' % HOST
        return
    print '*** Connected to host "%s"' % HOST

    try:
        f.login('acorn',"you'll never guess")
    except ftplib.error_perm:
        print 'ERROR: cannot login anonymously'
        f.quit()
        return
    print '*** Logged in as "acorn"'

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print 'ERROR: cannot CD to "%s"' % DIRN
        f.quit()
        return
    print '*** Changed to "%s" folder' % DIRN

    try:
        f.retrbinary('RETR %s' % FILE,open(FILE,'wb').write)
    except ftplib.error_perm:
        print 'ERROR: cannot read file "%s"' % FILE
        os.unlink(FILE) # 用于删除一个文件
    else:
        print '*** Downloaded "%s" to CWD' % FILE
    f.quit()
    return

if __name__ =='__main__':
    main()
 
