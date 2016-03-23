# encoding=utf-8
import urllib2
import urllib
import cookielib
import string
from sgmllib import SGMLParser
import re
import tkMessageBox
import os


def renrenBrower(url, user, password):
    # 登陆页面，可以通过抓包工具分析获得，如fiddler，wireshark
    login_page = "http://s1.mhjh.youqigame.com/uuu.php"
    try:
        # 获得一个cookieJar实例
        # cj = cookielib.CookieJar()
        # cookieJar作为参数，获得一个opener的实例
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        # 伪装成一个正常的浏览器，避免有些web服务器拒绝访问。
        opener.addheaders = [
            ('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36')]
        # 生成Post数据，含有登陆用户名密码。
        data = urllib.urlencode(
            {"loginname": user, "serverid": password, 'platform': 'uqee', 'fcm': 1, 'submit': '登陆'})
        print data
        # 以post的方法访问登陆页面，访问之后cookieJar会自定保存cookie
        op = opener.open(login_page, data)
        # 以带cookie的方式访问页面
        # op=opener.open(url)
        # 读取页面源码
        data = op.read()
        return data
    except Exception, e:
        print str(e)
Langs = ['debug', '', '', '', '', 'ko_kr']
ServerNames = ['ceshi1', 'ceshi2', 'ceshi3', 'ceshi4', 'ceshi5', 'ceshi6']


def loginCopy():
    # 获取flashvar
    print 'login--'
    htmldata = renrenBrower("http://s1.mhjh.youqigame.com", "10020544", "6")
    # htmldata = renrenBrower("http://s1.mhjh.youqigame.com", "86139192", "3")
    print 'get data back'
    reg = r"flashvars:'(.*?)'"
    m = re.search(reg, htmldata)
    w = m.group(1)
    os.chdir(r'C:\Users\admin\Desktop\python\debug')
    p = os.getcwd()
    p = p + r'\Preloader.html'
    print p
    # 修改Preloader文件

    with open(p, 'r') as f:
        filedata = f.read()
        wdata = r'window.location.href=window.location.href+"?dpmode=false&%s"' % w
        rdata = r'window.location.href=window.location.href+"?dpmode=false&server=six&debug=true&lang=ko_kr"'
        filedata = filedata.replace(rdata, wdata)
        tofile = r'D:\client1\project_six\xajh_Proj\xajh_Client_AS\xajhMain\bin-debug\Preloader.html'

        with open(tofile, 'w') as tof:

            tof.write(filedata)
            tof.close()
        f.close()
        tkMessageBox.showinfo("", "complete")

if __name__ == '__main__':
    loginCopy()
