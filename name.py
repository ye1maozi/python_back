# -*- coding:utf-8 -*
import xml.dom.minidom
import sys
reload(sys)
sys.setdefaultencoding('utf8')  
npc = 'npcshop.xml'
item = 'item.xml'

domNpc = xml.dom.minidom.parse(npc)
domItem = xml.dom.minidom.parse(item)

root = domItem.documentElement
itemObj = {}
itemlist = root.getElementsByTagName('item')
for item in itemlist:
    fileName = item.getAttribute('id')
    itemObj[fileName] = item.getAttribute('item_name')


root = domNpc.documentElement
itemlist = root.getElementsByTagName('mysteryshop')
names = []
for item in itemlist:
    fileName = item.getAttribute('id')

    names.append({'id': fileName, 'name': itemObj[
                 fileName], 'level': item.getAttribute('lv_need')})

def getStr(obj):
	s = '';
	for i in obj:
		s = s + i +":"+obj[i]
	return s+'\n'

with open("test.txt", "w") as tofile:
    for i in names:
        tofile.write(getStr(i))
    tofile.close()
