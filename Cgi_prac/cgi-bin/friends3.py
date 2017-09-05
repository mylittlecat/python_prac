#!/usr/bin/env python
# coding:utf-8

import cgi
from urllib import quote_plus
from string import capwords
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('friends')
logger.setLevel(logging.DEBUG) # logger的setLevel与handler的setLevel是不同的,但是一旦设置了logger对象,handler的(level)设置默认与logger对象一致(也就是说可以不设置handler的level,但反过来不行)
Rthandler = RotatingFileHandler('/home/bijy/python_prac/Cgi_prac/friends.log', mode = 'a', maxBytes=1024*1024, backupCount=5)
#Rthandler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
Rthandler.setFormatter(formatter)
logger.addHandler(Rthandler)


header = 'Content-Type: text/html\n\n'
url = '/cgi-bin/friends3.py'

errhtml = '''<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>'''

def showError(error_str):
    print header + errhtml % (error_str)

formhtml = '''<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>Friends list for: <I>%s</I></H3>
<FORM ACTION="%s">
<B>Your Name:</B>
<INPUT TYPE=hidden NAME=action VALUE=edit>
<INPUT TYPE=text NAME=person VALUE="%s" SIZE=15>
<P><B>How many friends do you have?</B>
%s
<P><INPUT TYPE=submit></FORM></BODY></HTML>'''

fradio = '<INPUT TYPE=radio NAME=howmany VALUE="%s" %s> %s\n'

def showForm(who, howmany):
    logger.info("howmany is:%s" % (howmany,))
    friends = ''
    for i in [0, 10, 25, 50, 100]:
        checked = ''
        if str(i) == howmany: # 一开始的比较全是false,因为即使howmany的初始值是0，也是int类型的，而左边是字符串类型的，随后，客户端返回的howmany变为字符串，就能产生True的结果
            logger.info("str(i) == howmany!!!")
            checked = 'CHECKED'
        friends = friends + fradio % \
            (str(i), checked, str(i))
    print header + formhtml % (who, url, who, friends)

reshtml = '''<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>Friends list for: <I>%s</I></H3>
Your name is: <B>%s</B><P>
You have <B>%s</B> friends.
<P>Click <A HREF="%s">here</A> to edit your data again.
</BODY></HTML>'''

def doResults(who, howmany):
    newurl = url + '?ation=reedit&person=%s&howmany=%s'%\
        (quote_plus(who), howmany)
    print header + reshtml % (who, who, howmany, newurl)

def process():
    error = ''
    form = cgi.FieldStorage()

    if form.has_key('person'):
        who = capwords(form['person'].value)
    else:
        who = 'NEW USER'

    if form.has_key('howmany'):
        howmany = form['howmany'].value
    else:
        if form.has_key('action') and \
                 form['action'].value =='edit':
            error = 'Please select number of friends.'
        else:
            howmany = 0

    if not error:
        if form.has_key('action') and \
                 form['action'].value != 'reedit':
            doResults(who, howmany)
        else:
            logger.info("first into 'if not error:...else:...'")
            showForm(who, howmany)
    else:
        showError(error)

if __name__ =='__main__':
    process()

