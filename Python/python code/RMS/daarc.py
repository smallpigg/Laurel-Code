#!/usr/bin/python
#coding:utf8

import struct

f = open('d261127','rb')

a = f.readline()
s = struct.unpack('11i',a[0:44])

