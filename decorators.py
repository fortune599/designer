import time

def runtime(f):
    stime = time.time()
    def inner(*arg):
        return f(*arg)
    etime = time.time()
    print "runtime of f: [%s]" % (str(etime - stime))
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

def memoize(f):
    memo = {}
    def inner(n):
        if n not in memo:
            memo[n] = f(n)
        return memo[n]
    return inner

@memoize
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

fib = runtime(fib)

#print listrange(1776, 2017, 4)
print fib(20)
