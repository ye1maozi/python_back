import os
import os.path
import time
import datetime

rootdir = "C:/Users/admin/Documents/My RTX Files/miaowenjie/"
os.chdir(rootdir)
files = os.listdir(rootdir)
suf = [".png", ".jpg", ".jpeg", ".gif"]
print "----- %s -----" % (" ".join(suf))


def inArray(fileName):
    fileName = fileName.lower()
    for n in suf:
        if n == fileName:
            return True
        pass
    return False


def deleteImg():
    # path = "C:/Users/admin/Documents/My RTX Files/docs"
    # if not os.path.exists(path):
    #     os.mkdir(path)

    now = datetime.datetime.now()
    b3 = datetime.timedelta(days=14)
    day3 = now - b3
    day3_timestamps = time.mktime(day3.timetuple())
    for name in files:
        p = os.path.splitext(name)

        # a = "%s/%s" % (path, name)
        if inArray(p[1]) :
            file_timestamp = os.path.getmtime(name)
            print name
            if float(file_timestamp) < float(day3_timestamps):
                # print "copy: %s" % a
                # print time.ctime(os.path.getmtime(name))
                # shutil.copy(name, a)
                os.remove(name)
                # os.utime(a, (file_timestamp, file_timestamp))
                # win32file.CopyFile(name,a,0)
    print 'out--------'
    os.system("start \"\" \"C:/Users/admin/Documents/My RTX Files/miaowenjie\"")

if __name__ == '__main__':
    deleteImg()