# -*- coding: cp936 -*-
import wx
import Export_Fun

class CreateMenu():
       def __init__(self,parent):
              self.menuBar=wx.MenuBar()
              self.file=wx.Menu()
              self.open=self.file.Append(-1,u'打开')
              #self.file.AppendSeparator()
              #self.close=self.file.Append(-1,u'退出')
              self.menuBar.Append(self.file,u'文件(&F)')
              parent.SetMenuBar(self.menuBar)
                    
class MyApp(wx.App):
       def OnInit(self):
              self.file=''
              self.width=300
              self.height=300
              self.frame=wx.Frame(parent=None,title='ExportDaarc',size=(self.width,self.height))
              self.panel=wx.Panel(self.frame,-1)
              self.menu=CreateMenu(self.frame)

# button----------------------------------------------------------------------------
              self.button = wx.Button(self.panel,-1,"雷达数据", pos=(100, 100))
              self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)  
              

              self.Bind(wx.EVT_MENU,self.OnOpen,self.menu.open)
              #self.Bind(wx.EVT_MENU,self.OnClose,self.menu.close)
              self.Bind(wx.EVT_SIZE,self.Resize)

              self.frame.Show()
              return True
       def OnOpen(self,event):
              dialog=wx.FileDialog(None,'ExportDaarc',style=wx.OPEN)
              if dialog.ShowModal()==wx.ID_OK:
                     self.file=dialog.GetPath()
                     #file=open(self.file)
                     #self.text.write(file.read())
                     #file.close()
              dialog.Destroy()
       
       #def OnClose(self,event):
              #self.frame.Destory()

       def OnClick(self,event):
              self.button.SetLabel("已转换")
              Export_Fun.RA_4000_alt(self.file)

       def Resize(self,event):
              newsize=self.frame.GetSize()
              width=newsize.GetWidth()-10
              height=newsize.GetHeight()-50

                           
app=MyApp()
app.MainLoop()
