#!/usr/bin/env python
# coding:utf-8

from socket import *
from time import ctime
from thread import start_new_thread

HOST = '' # HOST 变量为空，表示bind()函数可以绑定在所有有效的地址上 
PORT = 46973
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

def dealWithCli(tcpcs):
    'a new thread will call this function to deal with msg from client'
    while True:
        data = tcpcs.recv(BUFSIZ)
        if not data:
            break
        tcpcs.send('[%s] %s' % (ctime(),data))

    tcpcs.close()

if __name__ == "__main__":
    try:
        while True:
            print 'waiting for connection...'
            tcpCliSock, addr = tcpSerSock.accept()
            print '...connected from:',addr

            start_new_thread(dealWithCli,(tcpCliSock,))
    except (EOFError,KeyboardInterrupt), e:
        print 'Timestamp TCP server exit.',e
        tcpSerSock.close()
