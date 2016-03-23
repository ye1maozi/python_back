# -*- coding: UTF-8 -*-
from string import Template
add = lambda x, y: (
    x + y
)
print add(1, 2)
print 42
a = Template('$s this is $s')
print a.substitute(s='class')
print '%-05.1f' % 5.21

b = r' 1 '
print b.strip()

dit = {'a': 1, 'b': 2, 'c': 3}
for v in dit:
    print v
    print dit[v]
    break
else:
    print 'break'

s = r'%(a)s asd %(c)sasd %(b)ss' % dit
print s
if True and dit.get('d') != None:
    print "d"
elif True:
    print 'dd'

arr = [1, 2, 3]
print type(arr)


def param_test(x, y, *par, **dis):
    print x
    print y
    print par
    print dis

param_test(1, 2, 3, 4, 5, a=1, b=2)
apply


def f():
    fs = []
    for i in range(3):
        def g():
            return i * i
        fs.append(g)
    return fs

x, y, z = f()
print x()
import os

# root = r'D:/client1/project_six/xajh_Proj/xajh_Client_AS/res_module'
# os.chdir(root)
# os.system('git pull')

import copy
a = [n for n in dir(copy) if not n.startswith('_')]
print a
# import gittle
import re
print(re.escape('www.baidu.com'))


print "阿萨德"


sss = '''<tr class='asdd> </tr> 
asd
<tr class=sdasdasd></tr>'''
print sss

reg = '<tr class(.*?)</tr>'
m = re.findall(reg, sss)
print m