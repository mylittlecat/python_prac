# coding:utf-8
# 用于浏览新闻组信息的小程序
from nntplib import NNTP
from time import sleep
from traceback import format_exc
NNTP_server_list = ['news.newsfan.net','news.gmane.org','web.aioe.org']
def use_NNTP():
    for server in NNTP_server_list:
        print server
    server = raw_input('Which NNTP_server do you want to go?\n')
    while True:
        if server not in NNTP_server_list:
            print 'invalid srever name,try again!'
            server = raw_input()
        else:
            break
    s = NNTP(server)
    print "s = NNTP('news.newsfan.net') is OK!"
    (resp, lst) =s.list()
    while True:
        for i,elem in enumerate(lst):
            print i,elem[0].decode('gbk')
        num =raw_input('Which group do you want to go?\n')
        try:
            rsp, ct, first, last, grp = s.group(lst[int(num)][0])
            print "Article's range is:%s to %s." % (first,last)
            (resp, subs) = s.xhdr('subject',(str(first)+'-'+str(last)))
        except:
            print format_exc()
            print 'invalid input!try again!!!'
            sleep(3)
            continue
        for subject in subs:
            try:
                print subject[0],subject[1].decode('gbk')
            except:
                print subject[0],subject[1]
        while True: 
            try:
                number =raw_input('Which article do you want to read?\n')
                if number == 'q':
                    break
                f = open("NNTPfile",'w')
                (reply, num, id, list) = s.body(str(number),f)
                f = open("NNTPfile",'r')
                for eachLine in f:
                    try:
                        print eachLine.decode('gbk'),
                    except:
                        print eachLine
                f.close()
                print 'Press any to continue...(Press q to return...)'
                if raw_input() =='q':
                    break
            except:
                print format_exc()
                print 'invalid input!try again!!!'
                sleep(3)
    s.quit()
    return
def main():
    use_NNTP()

if __name__ =='__main__':
    main()
