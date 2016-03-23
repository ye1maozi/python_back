import threading
from Tkinter import *


def loop():
    print 'thread %s' % threading.current_thread().name


def startListening():
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print 'thread1 %s' % threading.current_thread().name


# startListening()


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.bind('<key>', self.printkey)#...

    def printkey(self,evt):
        print evt.char

app = Application()
app.master.title('aaa')

app.mainloop()
