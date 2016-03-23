# -*- coding:utf-8 -*
import urllib2
import urllib
import cookielib
import gzip
import StringIO
# url data timtoue
# response = urllib2.urlopen('http://www.baidu.com')
# print response.read()

# data = urllib.urlencode({"a": 1})
# # post
# req = urllib2.Request(url,data)
# # get
# url = ""+"?"+data

data = urllib.urlencode({"fid": 7, "rand": 673})
url = 'http://bbs.ngacn.cc/thread.php'
url = url + '?' + data
print url
cookie = cookielib.MozillaCookieJar("cookie_nga")
# cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
# handler.addheaders = [

# ]
hdrs = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Host': 'bbs.ngacn.cc',
        'Cookie': r'guestJs=1450147339'
        }
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)

req = urllib2.Request(url=url, headers=hdrs)

# req.add_header(
#     'User-agent', r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36')
# req.add_header(
#     'Accept', r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
# req.add_header('Accept-Encoding', r'gzip, deflate, sdch')
# req.add_header('Accept-Language', r'zh-CN,zh;q=0.8')
# req.add_header('Cache-Control', r'max-age=0')
# req.add_header('Connection', r'keep-alive')
# req.add_header('Upgrade-Insecure-Requests', '1')
# req.add_header('Host', r'bbs.ngacn.cc')

response = urllib2.urlopen(req)
# s = response.read()
# stream = StringIO.StringIO(s)
# with gzip.GzipFile(fileobj=stream) as f:
#     data = f.read()
# print(data)
# print len(s)
# print s
# cookie.save(ignore_discard=True, ignore_expires=True)
str1 = ''
lastUid = 0
for item in cookie:
    print "Name:" + item.name
    print "Value:" + item.value
    if item.name == 'lastvisit':
        val = int(item.value) - 10
        # val = 1450234212
        str1 = str1 + 'guestJs=' + str(val) + ';'
    str1 = str1 + item.name + '=' + item.value + ';'
print str1

print r'##########################################'
data = urllib.urlencode({"fid": -7})
url = 'http://bbs.bigccq.cn/thread.php'
url = url + '?' + data
print url
hdrs = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Host': 'bbs.bigccq.cn',
        "Referer": r'http://bbs.bigccq.cn/thread.php?fid=-7',
        'Cookie': r'guestJs=1450147339'
        }
hdrs["Cookie"] = str1
for item in hdrs:
    print '%s : %s' % (item, hdrs[item])

req = urllib2.Request(url=url, headers=hdrs)
response = urllib2.urlopen(req)
s = response.read()
# print s
stream = StringIO.StringIO(s)
with gzip.GzipFile(fileobj=stream) as f:
    data = f.read()
# print(data)
# print len(s)

print '%------------------------%'
from bs4 import BeautifulSoup
soup = BeautifulSoup(data)
from Tkinter import *
# import re
n=0;
for tag in soup.find_all("tr",attrs={'class':'topicrow'}):
    # if tag.get('class'):
    print tag.find_all('td',attrs={'class':'c2'})
    print tag['class']
    n= n+1;
    print '-----------'

print '&----------------&%d'%n
# reg = r'<tr class(.*?)</tr>'
# m = re.findall(reg, data,re.DOTALL)
# print m
