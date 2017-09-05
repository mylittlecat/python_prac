import logging
glb_dev_name_dict={'': 'NA', '192.168.1.6000c26033630': '\xe5\xa5\xa5\xe7\x89\xb9\xe6\x9b\xbc', '192.168.1.222001f2e00078f': '\xe8\x9c\x98\xe8\x9b\x9b\xe4\xbe\xa0'}
ScrIpNMac = '192.168.1.222001f2e00078f'
glb_dev_name_dict[ScrIpNMac] = glb_dev_name_dict[ScrIpNMac].decode("UTF-8")
print glb_dev_name_dict[ScrIpNMac]
logging.error(glb_dev_name_dict)
if ScrIpNMac in glb_dev_name_dict:
    print glb_dev_name_dict[ScrIpNMac]
else:
    print "No"
for elem in glb_dev_name_dict:
    print elem
