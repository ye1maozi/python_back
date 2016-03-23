import os
import os.path
import shutil

rootdir = "temp/"
files = os.listdir(rootdir)
for name in files:
    # print name
    if os.path.isfile(rootdir+name):
        p = os.path.splitext(name)

        path = rootdir + p[0];
        if not os.path.exists(path):
            os.mkdir(path)
        
        oldp = rootdir+name
        newp = "%s/%s" % (path, name)
        shutil.move(oldp,newp)

