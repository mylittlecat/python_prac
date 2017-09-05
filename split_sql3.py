#coding:utf-8
sql_str = """INSERT INTO incidents (status,sourceIp,destinationIp,action,protocol,appLayerProtocol,packetLength,riskLevel,signatureMessage,matchedKey,protocolDetail,timestamp,alertType,packet,sourceMac,destinationMac,dpi,dpiName,signatureName,signatureId,timestampint) values (0,'192.168.1.15','192.168.1.21',1,'TCP','NA',74,2,'','IP MAC Extra IP: (192.168.1.15) MAC: (00:50:56:2a:ce:ee) is Not in IP MAC List!','','2017-08-26T00:50:43Z',3,'NA','0050562aceee','f0761c6dad5d','192.168.1.15','192.168.1.21','3','0','1503679843865255')"""
#sql_str = """INSERT INTO incidents (status,sourceIp,destinationIp,action,protocol,appLayerProtocol,packetLength,riskLevel,signatureMessage,matchedKey,protocolDetail,timestamp,alertType,packet,sourceMac,destinationMac,dpi,dpiName,signatureName,signatureId) values (0,'192.168.1.6','192.168.1.222',1,'TCP','modbus',66,2,'(null)','Function: Read_Holding_Registers[3],startaddr:1000,endaddr:1000','{protocol:modbus,func:3,startaddr:1000,endaddr:1000}','2018-02-19T01:59:30Z',0,'001F2E00078F000C260336300800450000341CCC4000400699C3C0A80106C0A801DEC39C01F6011A836001618E2F501816D006E800002F4400000006010303E80001','000c26033630','001f2e00078f','192.168.1.6','192.168.1.222','1','200103')""" # 注意最新的版本最末尾还有一个timestampint字段
#sql_str = """INSERT INTO incidents (status,sourceIp,destinationIp,action,protocol,appLayerProtocol,packetLength,riskLevel,signatureMessage,matchedKey,protocolDetail,timestamp,alertType,packet,sourceMac,destinationMac,dpi,dpiName,signatureName,signatureId) values (0,'192.168.1.6','192.168.1.222',1,'TCP','modbus',66,2,'alert modbus, match all ','Function: Read_Holding_Registers[3],startaddr:1000,endaddr:1000','{protocol:modbus,func:3,startaddr:1000,endaddr:1000}','2017-08-14T20:58:42Z',0,'001F2E00078F000C26033630080045000034109240004006A5FDC0A80106C0A801DEC39C01F60119F0B4016107BC501816D02C410000230B00000006010303E80001','000c26033630','001f2e00078f','192.168.1.6','192.168.1.222','1','400003')"""
print """sql_str1.0 is:%s""" % (sql_str)
sql_str = sql_str[sql_str.find("values")+7:] # values 字符后面有一个空格需去除,所以下标要多1
print """sql_str2.0 is:%s""" % (sql_str)
sql_str = sql_str.strip("(")
sql_str = sql_str.strip(")")
print """sql_str3.0 is:%s""" % (sql_str)
sql_list = sql_str.split(",",8)
print """sql_list is:%s""" % (sql_list)
head_list = sql_list[:8]
print """head_list is:%s""" % (head_list)
middle_str = sql_list[8]
print """midddle_str is:%s""" % (middle_str)
middle_list = middle_str.split("'",6)
print """middle_list is:%s""" % (middle_list)
for i,elem in enumerate(middle_list):
    print i,elem
tail_str = middle_list[6]
print """tail_str is:%s""" % (tail_str)
tail_list = tail_str.strip(",").split(",")
print """tail_list is:%s""" % (tail_list)
elem_list = []
elem_list.extend(head_list)
elem_list.append(middle_list[1])
elem_list.append(middle_list[3])
elem_list.append(middle_list[5])
elem_list.extend(tail_list)
print """elem_list is:%s""" % (elem_list)
elem_list = [o.strip("""'""") for o in elem_list]
print """elem_list is:%s""" % (elem_list)
for i,elem in enumerate(elem_list):
    print i,elem
if elem_list[10] is None:
    print "elem_list[10] is:%s!" % (elem_list[10])
elif elem_list[10] is "":
    print "elem_list[10] is:%s!!" % (elem_list[10])
else:
    print "elem_list[10] is:%s!!!" % (elem_list[10])
