# -*- coding:utf-8 -*
import urllib2
import urllib
import cookielib
import os.path
import StringIO
import gzip
from bs4 import BeautifulSoup
from Tkinter import *
import threading
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
# 没有cookie 请求记录cookie

g_data = []
g_notify = False
g_ui = None
lock = threading.Lock()


def MainThread(flag):
    if flag:
        lock.release()
    else:
        lock.acquire()
        # thread1.pause()
        # thread2.pause()
    pass


class httpData(object):

    def no2GetCookie(self):
        # print 'no2GetCookie'
        cookie = cookielib.MozillaCookieJar("cookie_nga")
        handler = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(handler)
        url = 'http://bbs.ngacn.cc'
        opener.open(url)
        # cookie.save(ignore_discard=True, ignore_expires=True)
        return cookie
        pass

    # 获得cookie

    def getCookie(self):
            # 过期
        if None:  # os.path.exists("cookie_nga"):
            cookie = cookielib.MozillaCookieJar()
            cookie.load("cookie_nga")
        else:
            cookie = self.no2GetCookie()

        cookieStr = ''
        for item in cookie:
            # 登陆需要guestJs
            if item.name == 'lastvisit':
                val = int(item.value) - 10
                cookieStr = cookieStr + 'guestJs=' + str(val) + ';'

            cookieStr = cookieStr + item.name + "=" + item.value + ';'
        return cookieStr

    def loadHttp(self):
        # print 'loadHttp'
        cookieStr = self.getCookie()

        data = urllib.urlencode({'fid': -7})
        url = 'http://bbs.bigccq.cn/thread.php'
        url = url + '?' + data

        hdrs = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, sdch',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Host': 'bbs.bigccq.cn',
                "Referer": r'http://bbs.bigccq.cn/thread.php?fid=-7'
                }
        hdrs['Cookie'] = cookieStr
        print cookieStr

        req = urllib2.Request(url=url, headers=hdrs)
        response = urllib2.urlopen(req)
        s = response.read()
        # 乱码处理
        stream = StringIO.StringIO(s)
        with gzip.GzipFile(fileobj=stream) as f:
            data = f.read()

        # print data

        # parseHttpData(data)
        return data

    def parseHttpData(self):
        print 'parseHttpData'
        data = self.loadHttp()
        soup = BeautifulSoup(data)
        n = 0
        alist = []
        for tag in soup.find_all("tr", attrs={'class': 'topicrow'}):
            # print tag.find_all('td', attrs={'class': 'c2'})
            val = str(n)
            try:
                title = tag.find_all('a', attrs={'id': 't_tt' + val})[0]
                author = tag.find_all('td', attrs={'class': 'c3'})[0]
                replydate = tag.find_all('td', attrs={'class': 'c4'})[0]
                # print title
                # print author
                # print replydate
                dit = {
                    'title': title,
                    'author': author,
                    'replydate': replydate
                }
                alist.append(dit)
            except:
                pass
            # print '---------------'
            # print tag
            n = n + 1

        return alist


class Application(Frame):

    labelArr = []
    m_refresh = True
    urlArr = []

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        # self.Bind(wx.EVT_CLOSE, self.OnFormClosed, self)
        pass

    def createWidgets(self):

        # self.home = Button(self, text='home', command=self.onHome)
        # self.home.pack()
        self.txt = StringVar()
        self.txt.set('腿，大爷，小米，欧洲，恒大')
        entry = Entry(self, textvariable=self.txt, width=40)
        entry.pack()
        self.refresh = Button(self, text='stop', command=self.onRefresh)
        self.refresh.pack()
        # entry.bind("<Button-1>", self.handleradaptor(self.touchEntry, entry=entry))

        for i in range(0, 10):
            svar = StringVar()
            self.labelArr.append(svar)
            self.creaetLabel(svar, i)

    def leftClick(self, evt, name):
        print name
        

    def handleradaptor(self, fun, **kwds):
        return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)

    def creaetLabel(self, var, i):
        entry = Label(self, textvariable=var, width=40)
        # entry.bind("<Button-1>", self.handleradaptor(self.touchEntry, entry=entry))
        entry.bind('<Button-1>', self.handleradaptor(self.leftClick, name=i))
        entry.pack()
        pass

    def onRefresh(self):
        self.m_refresh = not self.m_refresh
        if self.m_refresh:
            self.refresh['text'] = 'stop'
        else:
            self.refresh['text'] = 'start'

        global MainThread
        MainThread(self.m_refresh)

        pass

    def onHome(self):
        pass

    def filter(self, filters, src):
        pass
        for item in filters:
            if src.find(item) != -1:
                return True

        return False

    def showList(self, data):
        print 'showlist'
        alen = len(self.labelArr)
        n = 0
        filters = self.txt.get()
        filters = filters.split('，')
        self.urlArr = []
        print filters
        for item in data:
            if n < alen:
                if self.filter(filters, item['title'].text):
                    self.labelArr[n].set(item['title'].text)
                    self.urlArr.append(item['title'])
                    n = n + 1
            else:
                break

        pass

    def quit(self):
        print 'quit'

    def OnFormClosed(self):
        print 'quit'


class UIthread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        # self.thread_num = num
        # self.interval = interval
        self.thread_stop = False

    def run(self):
        global g_data
        global g_notify
        global g_ui

        while not self.thread_stop:
            lock.acquire()
            if g_notify == True and g_ui != None:
                g_ui.showList(g_data)

            print 'UIthread'
            lock.release()
            time.sleep(5)
        pass

    def stop(self):
        print 'UIthread stop'
        self.thread_stop = True


class Reqthread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        # self.thread_num = num
        # self.interval = interval
        self.thread_stop = False

    def run(self):
        htp = httpData()
        global g_data
        global g_notify
        global g_ui

        while not self.thread_stop:
            lock.acquire()
            try:
                g_data = htp.parseHttpData()
                g_notify = True
                print g_notify
            finally:
                print 'Reqthread'
                lock.release()
                time.sleep(10)
            pass

    def stop(self):
        print 'Reqthread stop'
        self.thread_stop = True


if __name__ == "__main__":
    print '------------------start--------------------'
    thread1 = Reqthread()
    thread2 = UIthread()
    thread1.start()
    thread2.start()
    # loadHttp()
    g_ui = Application()
    g_ui.mainloop()

    thread1.stop()
    thread2.stop()
    print '------------------end--------------------'
