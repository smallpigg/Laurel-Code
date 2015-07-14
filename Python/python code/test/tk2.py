# -*- coding: utf8 -*-
from Tkinter import *
from FileDialog import *
 
root = Tk()
 
fd = LoadFileDialog(root) # 创建打开文件对话框
filename = fd.go() # 显示打开文件对话框，并获取选择的文件名称
print filename
 
root.mainloop()
