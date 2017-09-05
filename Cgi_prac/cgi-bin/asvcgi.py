#!/usr/bin/env python
# coding:utf-8

from cgi import FieldStorage
from os import environ
from cStringIO import StringIO
from urllib import quote, unquote
from string import capwords, strip, split, join
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('asvcgi')
logger.setLevel(logging.DEBUG) # logger的setLevel与handler的setLevel是不同的,但是一旦设置了logger对象,handler的(level)设置默认与logger对象一致(也就是说可以不设置handler的level,但反过来不行)
Rthandler = RotatingFileHandler('/home/bijy/python_prac/Cgi_prac/asvcgi.log', mode = 'a', maxBytes=1024*1024, backupCount=5)
#Rthandler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
Rthandler.setFormatter(formatter)
logger.addHandler(Rthandler)


class AdvCGI(object):

    header = 'Content-Type: text/html\n\n'
    url = '/cgi-bin/asvcgi.py'

    formhtml = '''<HTML><HAED><TITLE>
Advanced CGI Demo</TITLE></HEAD>
<BODY><H2>Advanced CGI Demo Form</H2>
<FORM METHOD=post ACTION="%s" ENCTYPE="multipart/form-data">
<H3>My Cookie Setting</H3>
<LI> <CODE><B>CPPuser = %s</B></CODE>
<H3>Enter cookie value<BR>
<INPUT NAME=cookie value="%s"> (<I>optional</I>)</H3>
<H3>Enter your name<BR>
<INPUT NAME=person VALUE="%s"> (<I>required</I>)</H3>
<H3>What languages can you program in?
(<I>at least one required</I>)</H3>
%s
<H3>Enter file to upload</H3>
<INPUT TYPE=file NAME=upfile VALUE="%s" SIZE=45>
<P><INPUT TYPE=submit>
</FORM></BODY></HTML>'''

    langSet = ('Python', 'PERL', 'Java', 'C++', 'PHP', 'C', 'JavaScript')

    langItem = \
    '<INPUT TYPE=checkbox NAME=lang VALUE="%s" %s> %s\n'

    def getCPPCookies(self): # read cookies from client
        if environ.has_key('HTTP_COOKIE'):
            for eachCookie in map(strip,\
                   split(environ['HTTP_COOKIE'], ';')):
                if len(eachCookie) > 6 and \
                           eachCookie[:3] == 'CPP':
                    tag = eachCookie[3:7]
                    try:
                        self.cookies[tag] = \
                            eval(unquote(eachCookie[8:]))
                    except (NameError, SyntaxError):
                        self.cookies[tag] = \
                             unquote(eachCookie[8:])
                else:
                    self.cookies['info'] = self.cookies['user'] = ''

        logger.info("self.cookies is:%s" % (self.cookies,))
        if self.cookies["info"]!= '':
            self.who, langStr, self.fn = \
                         split(self.cookies['info'],':')
            self.langs = split(langStr, ',')
        else:
            self.who = self.fn = ' '
            self.langs = ['Python']

    def showForm(self): # show fill-out form
        self.getCPPCookies()
        langStr = ''
        for eachLang in AdvCGI.langSet:
            if eachLang in self.langs:
                langStr += AdvCGI.langItem % \
                    (eachLang, ' CHECKED', eachLang)
            else:
                langStr += AdvCGI.langItem % \
                    (eachLang, '', eachLang)

        if not self.cookies.has_key('user') or \
               self.cookies['user'] == '':
            cookStatus = '<I>(cookies has not been set yet)</I>'
            userCook = ''
        else:
            userCook = cookStatus = self.cookies['user']

        print AdvCGI.header + AdvCGI.formhtml % (AdvCGI.url,
           cookStatus, userCook, self.who, langStr, self.fn)

    errhtml = '''<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>'''

    def showError(self):
        print AdvCGI.header + AdvCGI.errhtml % (self.error)

    reshtml = '''<HTML><HEAD><TITLE>
Advanced CGI Demo</TITLE></HEAD>
<BODY><H2>Your Uploaded Data</H2>
<H3>Your cookie value is: <B>%s</B></H3>
<H3>Your name is: <B>%s</B></H3>
<H3>You can program in the following languages:</H3>
<UL>%s</UL>
<H3>Your uploaded file...<BR>
Name: <I>%s</I><BR>
Contents:</H3>
<PRE>%s</PRE>
Click <A HREF="%s"><B>here</B></A> to return to form.
</BODY></HTML>'''

    def setCPPCookies(self): # tell client to store cookies
        for eachCookie in self.cookies.keys():
            print 'Set-Cookie: CPP%s=%s; path=/' % \
               (eachCookie, quote(self.cookies[eachCookie]))

    def doResult(self): # display result page
        MAXBYTES = 1024
        langlist = ''
        for eachLang in self.langs:
            langlist = langlist + '<LI>%s<BR>' % eachLang

        filedata = ''
        while len(filedata) < MAXBYTES: # read file chunks
            data = self.fp.readline()
            if data == '':break
            else:
                filedata += data
 
        self.fp.close()
        if filedata == '':
            filedata = \
        '<B><I>(file upload error or file not given)</I></B>'
        else:
            filedata += \
                 '... <B><I>(file truncated due to size)</I></B>'
        filename = self.fn

        if not self.cookies.has_key('user') or \
                 self.cookies['user'] == '':
            cookStatus = '<I>(cookie has not been set yet)</I>'
            userCook = ''
        else:
            userCook = cookStatus =self.cookies['user']

        self.cookies['info'] = join([self.who,\
            join(self.langs, ','), filename], ':')
        self.setCPPCookies()
        print AdvCGI.header + AdvCGI.reshtml % \
                (cookStatus, self.who, langlist,
                filename, filedata, AdvCGI.url)

    def go(self): # determine which page to return
        try:
            self.cookies = {}
            self.error = ''
            form = FieldStorage()
            if form.keys() == []:
                self.showForm()
                return

            if form.has_key('person'):
                logger.info("form['person'].value is:%s" % (form['person'].value,))
                self.who = capwords(strip(form['person'].value))
                if self.who == '':
                    self.error = 'Your name is required. (blank)'
            else:
                self.error = 'Your name is required. (missing)'

            if form.has_key('cookie'):
                logger.info("form['cookie'].value is:%s" % (form['cookie'].value,))
                self.cookies['user'] = unquote(strip(\
                                form['cookie'].value))
            else:
                self.cookies['user'] = ''

            self.langs = []
            if form.has_key('lang'):
                langdata = form['lang']
                if type(langdata) == type([]):
                    for eachLang in langdata:
                        self.langs.append(eachLang.value)
                else:
                    self.langs.append(langdata.value)
            else:
                self.error = 'At least one language required.'

            if form.has_key('upfile'):
                upfile = form["upfile"]
                self.fn = upfile.filename or ''
                if upfile.file:
                    self.fp = upfile.file
                else:
                    self.fp = StringIO('(no data)')
            else:
                self.fp = StringIO('(no file)')
                self.fn = ''

            if not self.error:
                self.doResult()
            else:
                self.showError()
        except:
            logger.exception("Error!!!")

if __name__ == '__main__':
    page = AdvCGI()
    page.go()
