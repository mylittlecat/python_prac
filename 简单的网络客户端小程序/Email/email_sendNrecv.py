#!/usr/bin/env python
# coding:utf-8
# 用于收发一封给自己邮箱邮件并比较是否有不同

from smtplib import SMTP_SSL
from poplib import POP3_SSL
from time import sleep

SMTPSVR = 'smtp.qq.com'
POP3SVR = 'pop.qq.com'

origHdrs = ['From: your qq email address',
    'To: your qq email address',
    'Subject: test msg']
origBody = ['xxx','yyy','zzz']
origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs),'\r\n'.join(origBody)])

sendSvr = SMTP_SSL(SMTPSVR)
sendSvr.login('Your qq email address','Your pwd')
errs = sendSvr.sendmail('Your qq email address',
     'Your qq email address',origMsg)
sendSvr.quit()
assert len(errs) == 0, errs
sleep(10) # wait for mail to be delivered

recvSvr = POP3_SSL(POP3SVR)
recvSvr.user('Your qq email address')
recvSvr.pass_('Your pwd')
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
# strip headers and compare to orig msg
sep = msg.index('')
recvBody = msg[sep+1:]
assert origBody ==recvBody # assert identical

