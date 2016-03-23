import os
import os.path
# import win32file
import shutil
import time
import datetime

files =None
suf = None
def init():
    rootdir = "C:/Users/admin/Documents/My RTX Files/miaowenjie/"
    os.chdir(rootdir)
    global files,suf
    files = os.listdir(rootdir)
    suf = [".xls", ".xlsx", ".xml", ".txt", ".doc", ".csv"]
    print "----- %s -----" % (" ".join(suf))


def inArray(fileName):
    for n in suf:
        if n == fileName:
            return True
        pass
    return False


def openDoc():
    global files,suf
    init();
    path = "C:/Users/admin/Documents/My RTX Files/docs"
    if not os.path.exists(path):
        os.mkdir(path)

    now = datetime.datetime.now()
    b3 = datetime.timedelta(days=3)
    day3 = now - b3
    day3_timestamps = time.mktime(day3.timetuple())
    for name in files:
        p = os.path.splitext(name)
        a = "%s/%s" % (path, name)
        if inArray(p[1]) and not os.path.exists(a):
            print name
            file_timestamp = os.path.getmtime(name)
            if float(file_timestamp) >= float(day3_timestamps):
                print "copy: %s" % a
                print time.ctime(os.path.getmtime(name))
                shutil.copy(name, a)
                os.utime(a, (file_timestamp, file_timestamp))
                # win32file.CopyFile(name,a,0)
    print 'out--------'
    os.system("start \"\" \"C:/Users/admin/Documents/My RTX Files/docs\"")

if __name__ == '__main__':
    openDoc()
