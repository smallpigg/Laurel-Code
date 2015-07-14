#!/usr/bin/python

n = 8589869056
j = 0
PN = [0 for x in range(5)]

while n == 8589869056:
    i = 1
    m = 0
    while i < n:
        if n%i == 0:
            m = m + i
        i = i + 1
    if m == n:
        print 'This is a perfect number:', m
        PN[j] = m
        j = j + 1
    elif n%1 == 0:
        print n
    n = n + 1
print 'The perfect number in this range:', PN

def yueshu(x1, x2)

n = x1

while n in range(x1,x2):
    i = 1
    m = 0
    while i < n:
        if n%i == 0:
            m = m + i
        i = i + 1
    if m == n:
        print 'This is a perfect number:', m
        PN[j] = m
        j = j + 1
    elif n%1 == 0:
        print n
    n = n + 1
print 'The perfect number in this range:', PN
