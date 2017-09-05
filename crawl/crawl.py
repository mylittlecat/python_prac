#!/usr/bin/env python
# coding:utf-8

from sys import argv
from os import makedirs, unlink, sep
from os.path import dirname, exists, isdir, splitext
from string import replace, find, lower
from htmllib import HTMLParser,HTMLParseError
from urllib import urlretrieve
from urlparse import urlparse, urljoin
from formatter import DumbWriter, AbstractFormatter
from cStringIO import StringIO
from time import sleep
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('Spiderman')
Rthandler = RotatingFileHandler('/home/bijy/python_prac/crawl/crawl.log', mode = 'a', maxBytes=1024,backupCount=5)
Rthandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
Rthandler.setFormatter(formatter)
logger.addHandler(Rthandler)

class Retriever(object):# download Wsb pages

    def __init__(self, url):
        self.url = url
        self.file = self.filename(url)

    def filename(self, url, deffile = 'index.html'):
        """用url的路径名部分创建文件夹"""
        parsedurl = urlparse(url, 'http:', 0) ## parse path
        path = parsedurl[1] + parsedurl[2]
        if parsedurl[2] == '': # 将路径格式转化为:www.xxx.com/,否则后面拆分会出错
            path += sep
        ext = splitext(path)
        if ext[1] == '': # no file, use default
            if path[-1] == '/': # 无论如何，将路径格式转化为:www.xxx.com/index.html的形式
                path+=deffile
            else:
                path+='/' + deffile
        ldir = dirname(path) # local directory, ldir是类似于www.xxx.com,表示主机的字符串
        print 'ldir is:%s' % (ldir,)
        if sep != '/': # os-indep. path separator 统一不同平台的文件分割符号
            ldir = replace(ldir, '/', sep)
        if not isdir(ldir): # create archive dir if nec.
            if exists(ldir):unlink(ldir)
            try:
                makedirs(ldir)
            except OSError, e:
                logger.error(e)
                logger.error("url is:%s\npath is:%s\nldir is:%s" % (url, path, ldir))
        print 'path is:%s' % (path,)
        return path

    def download(self):   # download Web page
        try:
            retval = urlretrieve(self.url, self.file)
        except IOError:
            retval = ('*** ERROR: invalid URL "%s"' %\
                self.url,)
        return retval

    def parseAndGetLinks(self):# parse HTML, save links
        self.parser = HTMLParser(AbstractFormatter(\
        DumbWriter(StringIO())))
        self.parser.feed(open(self.file).read())
        self.parser.close()
        return self.parser.anchorlist

class Crawler(object):# manage entire crawling process

    count = 0   # static downloaded page counter

    def __init__(self, url):
        self.q = [url]
        self.seen = []
        self.dom = urlparse(url)[1]

    def getPage(self, url):
        r = Retriever(url)
        retval = r.download()
        if retval[0] == '*': # error situation, do not parse
            print retval, '... skipping parse'
            return
        Crawler.count +=1
        print '\n(', Crawler.count, ')'
        print 'URL:', url
        print 'FILE:', retval[0]
        self.seen.append(url)

        links = r.parseAndGetLinks() # get and process links
        print "link list is:%s" % (links,)
        for eachLink in links:
            if eachLink[:4] != 'http' and \
                    find(eachLink, '://') == -1:
                eachLink = urljoin(url, eachLink)
            print '*', eachLink,

            if find(lower(eachLink), 'mailto:') != -1:
                print '... discarded, mailto link'
                continue

            if eachLink not in self.seen:
                if find(eachLink, self.dom) == -1: # 属于其他域的链接(本程序只爬一个域的链接，否则文件很多)
                    print '... discarded, not in domain'
                else:
                    if eachLink not in self.q:
                        self.q.append(eachLink)
                        print '... new, added to Q'
                    else:
                        print '... discarded, already in Q' # 已在队列中待处理的链接
            else:
                print '... discarded, already processed' # 已经下载过的链接

    def go(self):# process links in queue
        while self.q:
            try:
                url = self.q.pop()
                self.getPage(url)
            except HTMLParseError, e:
                logger.exception('Exception:HTMLParseError!')

def main():
    if len(argv)> 1:
        url = argv[1]
    else:
        try:
            url = raw_input('Enter starting URL: ')
        except (KeyboardInterrupt, EOFError):
            url = ''
    if not url:return
    robot = Crawler(url)
    robot.go()

if __name__ =='__main__':
    main()

