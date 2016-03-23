import xml.dom.minidom
import os
# dirRoot = r"D:/client1/project_six/xajh_Proj/xajh_Client_AS/res_module/xajh_resource/config/zh_tw/mb/"
# dirRoot = r'D:/client1/project_six/xajh_Proj/xajh_Client_AS/res_module/xajh_resource/config/vi_vn/'

# os.chdir(dirRoot)
# files = os.listdir(dirRoot)
# for name in files:
#     print name

xmlpath = r'rp_list_zh_tw.xml'
# xmlpath = r'rp_list_vi_vn.xml'
dom = xml.dom.minidom.parse(xmlpath)
root = dom.documentElement
eles = [r'resource/model/mount/mount_10045',
        r'resource/model/mount/mount_10040'
        ]


def infind(fileName):
    for name in eles:
        if fileName.find(name) != -1:
            return True
    return False
itemlist = root.getElementsByTagName('rp')
for item in itemlist:
    fileName = item.getAttribute('file')
    # print fileName
    if infind(fileName):
        print fileName
        item.setAttribute('md5', '1')

root.toxml()
with open('rp_list_zh_tw.xml', 'w') as f:
    f.write(root.toxml())
    f.close()
# print root.nodeName
# find
# item = xml.dom.minidom.parse("item.xml")
# bag = xml.dom.minidom.parse("ttt.xml")
# root = item.documentElement
# itemlist = root.getElementsByTagName('item')
# baglist = bag.documentElement.getElementsByTagName('question')

# find = False
# n = 0;
# for j in baglist:
#     find = False
#     bid = j.getAttribute('id')
#     for i in itemlist:
#         tid = i.getAttribute('id')
#         if tid == bid:
#             find = True
#             break;

#     if find == False:
#         print 'not find%s'%bid
#     else:
#         n += 1
#         print 'find %s'%bid


# print n
