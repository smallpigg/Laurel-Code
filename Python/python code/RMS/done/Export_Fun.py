#!/usr/bin/python
#coding:utf-8

import struct

def RA_4000_alt(filepath):
    '转换RA_4000雷达高度计数据函数'
    f = open(filepath)
    savepath = filepath[-len(filepath):-4]+'_alt.txt'
    t = open(savepath,'w')

    str1 = '1'    

    while str1:
        str1 = f.readline()
        if str1[9:15]=='000000':
            Altitude = struct.unpack('<h',str1[22:20:-1])
            str2 = str(Altitude[0])
            str0 = str1[0:18] + str2 + '\n'
            t.write(str0)

    f.close()
    t.close()

"""
def D_file():
def S1_file():
def S2_file():
def S3_file():
def S4_file():
def E_file():
def A_file():
"""
