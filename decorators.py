import time

def runtime(f):
    def inner(*arg):
        stime = time.time()
        ret = f(*arg)
        etime = time.time()
        print "runtime of %s: [%s]" % (f.func_name, str(etime - stime))
        return ret
    return inner

def fxinf(f):
    def inner(*args):
        print "%s%s" % (f.func_name, args)
        return f(*args)
    return inner

@runtime
@fxinf
def listrange(first, last, interval):
    ret = []
    for i in range(first, last + 1):
        if (i % interval == 0):
            ret.append(i)
    return ret

print listrange(1776, 2017, 4)
