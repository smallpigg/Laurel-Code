#!/usr/bin/python

def yueshu(x):

n = x

if (x-int(x))!=0 or x<=0:
    print 'I reject to compute!!!'
else:
    i = 1
    for i <= n:
        if n%i == 0:
            m += [i]
            m += [n/i]
            i += 1
        n = int(n/(i-1))
return (m,len(m))
