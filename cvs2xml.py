# -*- coding:utf-8 -*
# import csv
# with open('items.csv', 'rb') as f:
#     # reader = csv.reader(f)
#     reader = csv.DictReader((line.replace('\0','') for line in f),delimiter=",");
#     for row in reader:
#         print row
import xlrd
import xml.dom
from Tkinter import *
import os
import tkMessageBox
import xml.dom.minidom
#text中文不能输出
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
# data = xlrd.open_workbook("items.xls")
# table = data.sheets()[0]
# print data.sheet_names()
# # 行数
# nrows = table.nrows
# # 列数
# ncols = table.ncols
# print nrows
# print ncols
# colnames = table.row_values(0)
# for rownum in colnames:
#     print type(rownum)

# print 'asd%s ada%s' % (1, '3')
# print len(data.sheets())
# ui类


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def onSearch(self):
        dress = self.dress.get()
        # root = os.getcwd()

        # root = root + '/' + dress
        # print root
        p = os.path.splitext(dress)
        name = os.path.split(p[0])[1]
        print name
        if not p[1] or (p[1] != '.csv' and p[1] != '.xls' and p[1] != '.xlsx'):
            tkMessageBox.showinfo("", ".csv/.xls/.xlsx")
            return

        if os.path.exists(dress):
            print 'exists'
            self.openFile(dress)
        else:
            tkMessageBox.showinfo("", "file not exist")
    # 点击选中全部
    # def touchEntry(self, evt, entry):
    #     print entry
    #     text = entry.get()
    #     print len(text) 
    #     entry.selection_range(0,10)
    #     pass

    def handleradaptor(self, fun, **kwds):
        return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)

    def createEntry(self, txt):

        entry = Entry(self, textvariable=txt, width=40)
        # entry.bind("<Button-1>", self.handleradaptor(self.touchEntry, entry=entry))
        entry.pack()

    def createWidgets(self):
        self.dress = StringVar()
        self.dress.set('文件名 相对/绝对')
        self.createEntry(self.dress)

        self.sheets = StringVar()
        self.sheets.set('表 格式 0,2(第1,3表)')
        self.createEntry(self.sheets)

        self.ncols = StringVar()
        self.ncols.set('列 格式 1-3:0,4(上面第一个的2-4列,第二个的1,5列)')
        self.createEntry(self.ncols)
# key名称
        self.search = Button(self, text='search', command=self.onSearch)
        self.search.pack()

    # 主要处理
    def openFile(self, file):
        p = os.path.splitext(file)
        name = os.path.split(p[0])[1]
        data = xlrd.open_workbook(file)
        sheets = self.sheets.get()
        sheetslist = sheets.split(',')
        print sheetslist
        ncols = self.ncols.get()
        ncolslist = ncols.split(':')
        print ncolslist
        doc = xml.dom.minidom.Document()
        rootEle = doc.createElement(name)
        doc.appendChild(rootEle)
        # sheet循环
        for i in range(len(sheetslist)):
            ii = sheetslist[i]

            table = data.sheets()[int(ii)]
            if not table:
                tkMessageBox.showinfo("", "sheet %d not exist" % i)
                return
            sheetname = data.sheet_names()[i].encode('utf-8')
            sheetEle = doc.createElement(sheetname)
            rootEle.appendChild(sheetEle)
            print '---------%d' % i
            curcols = ncolslist[i]
            num = []

            # ncols 判断
            if curcols.find('-') != -1:
                arr = curcols.split('-')
                if arr[0] > arr[1]:
                    tkMessageBox.showinfo(
                        "", "sheet %s table %s" % (i, curcols))
                    return
                n1 = int(arr[0])
                n2 = int(arr[1]) + 1
                while n1 < n2:
                    num.append(n1)
                    n1 += 1
            elif curcols.find(','):
                arr = curcols.split(',')
                num = arr
            else:
                num.append(curcols)

            # key名称
            colnames = table.row_values(0)
            names = []

            for rownum in colnames:
                names.append(rownum)
            # xls to xml
            print '............%d' % table.nrows
            print num
            for nrow in range(1, table.nrows):
                item1 = doc.createElement("%slist" % sheetname)
                for ncol in num:
                    value = table.cell(nrow, int(ncol)).value
                    if isinstance(value, float):
                        val = '%0d' % value
                    else:
                        val = value.encode('utf-8')

                    item1.setAttribute(names[int(ncol)], val)
                    # print('%s : %s' % (names[int(ncol)], val))

                sheetEle.appendChild(item1)
        # 当前目录创建xml/...
        f = open(name + '.xml', 'w')
        # doc.writexml(f)
        f.write(doc.toprettyxml())
        f.close()
        tkMessageBox.showinfo("", "complete")
        pass

if __name__ == "__main__": 
    app = Application()
    app.master.title('xls/cvs/xlsx2xml')
    app.width = 300
    app.mainloop()
