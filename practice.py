#!/usr/bin/env python 
#-*- coding:utf-8 -*-	
#第一行为直接运行脚本命令
#第二行为UTF—8编码命令
import re
patt="(\d+\.\d+\.\d+\.\d+).*?(\d+\.\d+\.\d+\.\d+).*sid:(\d+)"#取IP地址字符串和sid字符串
filename="rulefile.txt"
fobj=open(filename,'r+')
str1=fobj.read()
m=re.search(patt,str1)#寻找IP地址字符串和sid字符串
id1=m.group(1)+" "#注意末尾要加" "以标记替换整个IP地址
id2=m.group(2)+" "
sid=int(m.group(3))
idstr=id2.split(".")#分割后两位IP地址
a=int(idstr[3])#转化分割的IP地址为整型
b=int(idstr[2])#同上
while a!=254 or b!=200:#a是最后八位IP地址，b是倒数第二个八位IP地址
    rs1="%d.%d " % (b,a)#注意末尾加" "
    if a==254 and b!=200:
        b+=1
        a=0
    else:
        a+=1
    rs2="%d.%d " % (b,a)
    new_sid=str(sid+1)
    new_str=id2.replace(rs1,rs2)#生成新的IP地址（递增1）
    str1=str1.replace(id2,new_str)#先换第二个出现的IP地址以免中途出现重复字符
    temp=id2#保存第二个IP地址值备用
    str1=str1.replace(id1,id2)#再换第一个IP地址
    id2=new_str#更新第二个IP地址值
    id1=temp#更新第一个IP地址值
    str1=str1.replace(str(sid),new_sid)#递增sid值
    sid+=1#更新sid值
    fobj.write(str1)#写入文件里
#	调试代码块:
#	count+=1 
#	if count>5:
#		break
fobj.close()#关闭文件
