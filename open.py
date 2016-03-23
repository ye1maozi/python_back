# -*- coding: utf-8 -*-
import os
import os.path
from Tkinter import *
# 自定义模版
import getDoc
import login
import xcpoy
# 需要打开路径/文件
paths = [r'D:/client1/project_six/xajh_Proj/xajh_Client_AS/res_module/xajh_tools/mhjh_mobileclient/Debug.win32/MHJHJavascript_d.exe',
         r'D:/client1/project_six/xajh_Proj/xajh_Client_AS/res_module',
         r'D:/client1/project_six/xajh_Proj/xajh_Client_AS/xajhMain',
         r'D:/client/wly_client_as',
         r'D:/client/wly_resource',
         r'D:/client1/project_six_doc'
         ]

# ui类


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def leftClick(self, evt, name):
        if os.path.isfile(name):
            arr = os.path.split(name)
            os.chdir(arr[0])  # 不在当前目录打开有问题。。。
            cdp = "start \"\" \"%s\"" % (arr[1])
            os.system(cdp)
            # print cdp
        else:
            path = "start \"\" \"%s\"" % name
            os.system(path)

    def rightClick(self, evt, name):
        if os.path.isfile(name):
            arr = os.path.split(name)
            path = "start \"\" \"%s\"" % arr[0]
            os.system(path)
            pass
        else:
            os.chdir(name)
            os.system('start cmd.exe')

            pass

    def loginCopy(self):
        login.loginCopy()

    def getDoc(self):
        getDoc.openDoc()

    def Copy(self):
        self.flag = not self.flag
        if self.flag:
            # xcpoy.create()
            self.createApp()
        else:
            self.app.forget()

    def createWidgets(self):

        for name in paths:
            self.createButton(name)

        Button(self, text='login', command=lambda: self.loginCopy()).pack()
        Button(self, text='getDoc', command=lambda: self.getDoc()).pack()
        Button(self, text='copy', command=lambda: self.Copy()).pack()
        self.flag = False

        # quitButton = Button(self, text='quit')
        # quitButton.bind('<Button-1>', self.handleradaptor(self.handler, a=1))
        # quitButton.bind('<Button-3>', self.rightClick)
        # quitButton.pack()

    # def leftClick(self, evt, name):
    #     print evt.type

    # def rightClick(self, evt, name):
    #     print 'right'

    def createButton(self, name1):
        arr = os.path.split(name1)
        name = arr[1]
        path = arr[0]
        print '%s:%s' % (name, path)
        btn = Button(self, text=name)
        btn.bind('<Button-1>', self.handleradaptor(self.leftClick, name=name1))
        btn.bind('<Button-3>', self.handleradaptor(self.rightClick, name=name1))
        btn.pack()

    # def handler(self, event, a):
    #     print a

    def handleradaptor(self, fun, **kwds):
        return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)

    def createApp(self):
        if not hasattr(self,'app'):
            rootdir = "D:/client1/project_six/xajh_Proj/xajh_Client_AS/"
            os.chdir(rootdir)
            files = os.listdir(rootdir)
            self.app = xcpoy.Select()
            self.app.master.title('copy resouce')
        self.app.pack()


app = Application()
app.master.title('aaa')

app.mainloop()
