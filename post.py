# -*- coding:utf-8 -*
import urllib2
import urllib
import cookielib
import gzip
import StringIO
# url data timtoue
url = 'http://127.0.0.1:3000'
# response = urllib2.urlopen()
# print response.read()

data = urllib.urlencode({"a": 1})
# # post
req = urllib2.Request(url,data)
# # get
# url = ""+"?"+data
response = urllib2.urlopen(req)
s = response.read()
print s