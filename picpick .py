# -*- coding: utf-8 -*-
import urllib2
import re
import urllib
import os.path
import os


def getData():
    url = r'http://www.ivsky.com/tupian/'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()
    return data


def savePic(data):
    reg = r'<img src="(.*?)"'
    if not os.path.exists(r'temp'):
        os.mkdir('temp')
    m = re.findall(reg, data, re.S)
    for i in m:
        arr = i.split(r'/')
        name = arr[len(arr) - 1]
        urllib.urlretrieve(i, r'temp/%s' % name)

data = getData()
savePic(data)
