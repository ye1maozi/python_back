import os


def count():
    fs = []
    for i in range(1, 4):
        #		def f(j):
        def g():
            return i * i
#			return g
        fs.append(g())
    return fs

f1, f2, f3 = count()
print f1
print f2
print f3
try:
    f = open("test.txt", "r")
    # print f.read();
    for line in f.readlines():
        print(line.strip())
finally:
    if f:
        f.close()

path = os.path.abspath(".")
path = os.path.join(path, "fileDemo")
print path
if not os.path.exists(path):
    os.mkdir(path)
    print "create"

print "--------------"
try:
    url = os.path.join(path, "out.txt")
    print(url)
    f1 = open(url, "w")
except Exception, e:
    print "error"

try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name="a", age="1")
pickle.dump(d, f1)
f1.close()
