# File: hello2.py
#coding:utf8

from Tkinter import *
 
# 将子控件打包在App类，并绑定到相同的成员方法
class App:
 
    def __init__(self, master):
 
        frame = Frame(master)
        frame.pack()
 
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)
 
        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)
 
    def say_hi(self):
        print "hi there, everyone!"
 
root = Tk()
 
app = App(root) #实例化时传入root节点
 
root.mainloop() #同样启动事件循环
