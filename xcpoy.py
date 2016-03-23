# -*- coding: utf-8 -*-
import os
import Tkinter
import ttk
from Tkinter import *
import shutil
import tkMessageBox
# def click():
#     print variable.get()
#     pass

# master = Tkinter.Tk()

# variable = Tkinter.StringVar(master)
# variable.set("one")  # default value

# w = ttk.Combobox(master, textvariable=variable, values=["one", "two", "three"])
# w.pack()
# btn = Button(master, text="name", command=lambda: click())
# btn.pack();
# master.mainloop()
# relateObj = {'src': {'xajhMain': r'xajhMain/bin - debug/',
#                      'res_module': r'es_module/xajh_resource/'},
#              'lang': {'zh_cn': 'zh_cn',
#                       'ko_kr': 'ko_kr',
#                       'vi_vn': 'vi_vn',
#                       'zh_tw': 'zh_tw'},
#              'data': {'swf': 0, 'data': 1, 'all': 2}
#              }


class Select(Frame):
    variables = {}
    relateObj = {'src': {'xajhMain': r'xajhMain/bin-debug/',
                         'res_module': r'res_module/xajh_resource/'},
                 'lang': {'zh_cn': 'zh_cn',
                          'ko_kr': 'ko_kr',
                          'vi_vn': 'vi_vn',
                          'zh_tw': 'zh_tw'},
                 'data': {'swf': 0, 'data': 1, 'all': 3}
                 }

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        for var in self.relateObj:
            self.createCombobox(var)
        Button(self, text="copy", command=lambda: self.click()).pack()
        self.labeltxt =  StringVar()
        Label(self, textvariable=self.labeltxt).pack()
        # self.btn = Button(self, text="copy", command=lambda: self.click1())
        # self.btn.pack()

    def click1(self):
        self.btn.forget()

    def createCombobox(self, var):
        # print var
        Label(self, text=var).pack()

        self.variables[var] = StringVar()
        v = self.getArray(var)
        if len(v) > 0:
            self.variables[var].set(v[0])
            w = ttk.Combobox(self, textvariable=self.variables[var],
                             values=v)
            w.config(state="readonly")
            w.pack()

    def getArray(self, str):
        arr = []
        obj = self.relateObj[str]
        if obj:
            for n in obj:
                arr.append(n)
        return arr

    def click(self):
        
        toPath = self.variables["src"].get()
        toPath = self.relateObj['src'][toPath]
        fromPath = 'res_module/'
        lang = self.variables["lang"].get()
        data = self.variables["data"].get()
        print toPath
        print lang
        print data

        if data == "swf" or data == "all":
            if lang == 'zh_cn':
                fromPathSwf = fromPath + r'xajh_resource/resource/ui/swf/swf_debug/'
            else:
                fromPathSwf = fromPath + 'multilateral/' + lang + \
                    '_resource/resource/ui/swf/swf_debug/'
       
        if data == "swf" or data == "all":
            tpath = toPath + 'resource/ui/swf/swf_debug/'
            self.copySwf(tpath, fromPathSwf)

        self.labeltxt.set("start...")
        if data == "data" or data == "all":
            tpath = toPath + 'resource/logicdata/debug/'
            fpath = fromPath + 'xajh_resource/resource/logicdata/debug/'
            self.copyData(tpath, fpath)

        self.labeltxt.set("complete...")
        tkMessageBox.showinfo("", "complete")

    def copySwf(self, t, f):
        # print "copy swf from :%s , to: %s" % (f, t)
        # cmd = r'echo a|xcopy /s %s.swf %spath'%(f,t)
        # print cmd
        # os.system(cmd)
        files = os.listdir(f)
        for n in files:
            p = os.path.splitext(n)
            if p[1] == ".swf":
                # pass
                fn = "%s%s" % (f, n)
                tn = "%s%s" % (t, n)
                shutil.copy(fn, tn)
                # print "copy swf from :%s , to: %s" % (fn, tn)
        pass

    def copyData(self, t, f):
        # print "copy data from :%s , to: %s" % (f, t)
        # cmd = r'echo a|xcopy %s*.* %spath'%(f,t)
        # print cmd
        # os.system(cmd)
        # os.system("pause")
        files = os.listdir(f)
        for n in files:
            print n
            fn = "%s%s" % (f, n)
            tn = "%s%s" % (t, n)
            print tn
            shutil.copy(fn, tn)
        pass

def create():
    rootdir = "D:/client1/project_six/xajh_Proj/xajh_Client_AS/"
    os.chdir(rootdir)
    files = os.listdir(rootdir)
    app = Select()
    app.master.title('copy resouce')
    app.mainloop()

if __name__ == "__main__":
    create()
