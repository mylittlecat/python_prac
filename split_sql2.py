# coding:utf-8
sql_str = """INSERT INTO incidents (status,sourceIp,destinationIp,action,protocol,appLayerProtocol,packetLength,riskLevel,signatureMessage,matchedKey,protocolDetail,timestamp,alertType,packet,sourceMac,destinationMac,dpi,dpiName,signatureName,signatureId) values (0,'192.168.1.6','192.168.1.222',1,'TCP','modbus',66,2,'(null)','Function: Read_Holding_Registers[3],startaddr:1000,endaddr:1000','{protocol:modbus,func:3,startaddr:1000,endaddr:1000}','2018-02-19T01:59:30Z',0,'001F2E00078F000C260336300800450000341CCC4000400699C3C0A80106C0A801DEC39C01F6011A836001618E2F501816D006E800002F4400000006010303E80001','000c26033630','001f2e00078f','192.168.1.6','192.168.1.222','1','200103')""" # 现在更新的版本会在语句的最末尾追加一个timestampint字段
#sql_str = """INSERT INTO incidents (status,sourceIp,destinationIp,action,protocol,appLayerProtocol,packetLength,riskLevel,signatureMessage,matchedKey,protocolDetail,timestamp,alertType,packet,sourceMac,destinationMac,dpi,dpiName,signatureName,signatureId) values (0,'192.168.1.6','192.168.1.222',1,'TCP','modbus',66,2,'alert modbus, match all ','Function: Read_Holding_Registers[3],startaddr:1000,endaddr:1000','{protocol:modbus,func:3,startaddr:1000,endaddr:1000}','2017-08-14T20:58:42Z',0,'001F2E00078F000C26033630080045000034109240004006A5FDC0A80106C0A801DEC39C01F60119F0B4016107BC501816D02C410000230B00000006010303E80001','000c26033630','001f2e00078f','192.168.1.6','192.168.1.222','1','400003')"""
print """sql_str1.0 is:%s""" % (sql_str)
sql_str = sql_str[sql_str.find("values")+7:] # values 字符后面有一个空格需去除,所以下标要多1
print """sql_str2.0 is:%s""" % (sql_str)
sql_str = sql_str.strip("(")
sql_str = sql_str.strip(")")
print """sql_str3.0 is:%s""" % (sql_str)
sigMsg = sql_str[(sql_str[:(sql_str.find("Function")-3)].rfind("'")):(sql_str.find("Function")-1)]
print sigMsg
sql_str = sql_str.replace(sigMsg,"")
print sql_str
rule_str = sql_str[(sql_str.find("Function")-1):(sql_str.find("{")-1)]
print rule_str
sql_str = sql_str.replace(rule_str,"")
print sql_str
detail_str = sql_str[(sql_str.find("{")-1):(sql_str.find("}")+3)]
print detail_str
sql_str = sql_str.replace(detail_str,"")
print sql_str
sigMsg = sigMsg.strip(',').strip("""'""")
print sigMsg
rule_str = rule_str.strip(',').strip("""'""")
print rule_str
detail_str = detail_str.strip(',').strip("""'""")
print detail_str
sql_list = sql_str.split(",")
#sql_list[12] = ','.join(sql_list[12:16])
#print sql_list[12]
#del sql_list[13:16]
#sql_list[9] = ','.join(sql_list[9:12])
#print sql_list[9]
#del sql_list[10:12]
#print sql_list
sql_list = [o.strip("""'""") for o in sql_list]
print sql_list
sql_list.insert(8,sigMsg)
sql_list.insert(9,rule_str)
sql_list.insert(10,detail_str)
for i,elem in enumerate(sql_list):
    print i,elem
#if sql_list[1] == "192.168.1.6":
#    print "yes!!!"
#else:
#    print "No!!!"
#    print "192.168.1.6"
#    print sql_list[1]
