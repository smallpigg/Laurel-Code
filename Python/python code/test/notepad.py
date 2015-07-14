# -*- coding: cp936 -*-
import wx
 
class CreateMenu():
       def __init__(self,parent):
              self.menuBar=wx.MenuBar()
              self.file=wx.Menu()
              self.open=self.file.Append(-1,u'��')
              self.save=self.file.Append(-1,u'����')
              self.saveas=self.file.Append(-1,u'���Ϊ')
              self.file.AppendSeparator()
              self.close=self.file.Append(-1,u'�˳�')
              self.menuBar.Append(self.file,u'�ļ�(&F)')
              self.edit=wx.Menu()
              self.undo=self.edit.Append(-1,u'����')
              self.redo=self.edit.Append(-1,u'����')
              self.edit.AppendSeparator()
             
              self.cut=self.edit.Append(-1,u'����')
              self.copy=self.edit.Append(-1,u'����')
              self.paste=self.edit.Append(-1,u'ճ��')
              self.edit.AppendSeparator()
              self.selectall=self.edit.Append(-1,u'ȫѡ')
              self.menuBar.Append(self.edit,u'�༭(&E)')
             
              self.view=wx.Menu()
              self.color=self.view.AppendCheckItem(1051,u'��Ϊ��ɫ')
              self.trans=self.view.Append(-1,u'����͸����')
              self.menuBar.Append(self.view,u'�鿴(&V)')
             
              self.help=wx.Menu()
              self.about=self.help.Append(-1,u'����')
              self.menuBar.Append(self.help,u'����(&H)')
              parent.SetMenuBar(self.menuBar)
             
class MyApp(wx.App):
       def OnInit(self):
              self.file=''
              self.width=600
              self.height=480
              self.frame=wx.Frame(parent=None,title='wxpython Notebook',size=(self.width,self.height))
              self.panel=wx.Panel(self.frame,-1)
              self.menu=CreateMenu(self.frame)
              self.text=wx.TextCtrl(self.panel,-1,pos=(2,2),size=(self.width-10,self.height-50),
                        style=wx.HSCROLL|wx.TE_MULTILINE)
             
              self.Bind(wx.EVT_MENU,self.OnOpen,self.menu.open)
              self.Bind(wx.EVT_MENU,self.OnSave,self.menu.save)
              self.Bind(wx.EVT_MENU,self.OnSaveAs,self.menu.saveas)
              self.Bind(wx.EVT_MENU,self.OnClose,self.menu.close)
              self.Bind(wx.EVT_MENU,self.OnUndo,self.menu.undo)
              self.Bind(wx.EVT_MENU,self.OnRedo,self.menu.redo)    
              self.Bind(wx.EVT_MENU,self.OnCut,self.menu.cut)
              self.Bind(wx.EVT_MENU,self.OnCopy,self.menu.copy)
              self.Bind(wx.EVT_MENU,self.OnPaste,self.menu.paste)
              self.Bind(wx.EVT_MENU,self.OnSelectAll,self.menu.selectall)
              self.Bind(wx.EVT_MENU,self.OnColor,self.menu.color)
              self.Bind(wx.EVT_MENU,self.OnTrans,self.menu.trans)
              self.Bind(wx.EVT_MENU,self.OnAbout,self.menu.about)
 
              self.Bind(wx.EVT_RIGHT_DOWN,self.OnRClick)
              self.Bind(wx.EVT_SIZE,self.Resize)
              self.frame.Show()
              return True
       def OnOpen(self,event):
              dialog=wx.FileDialog(None,'wxpython Notebook',style=wx.OPEN)
              if dialog.ShowModal()==wx.ID_OK:
                     self.file=dialog.GetPath()
                     file=open(self.file)
                     self.text.write(file.read())
                     file.close()
              dialog.Destroy()
       def OnSave(self,event):
              if self.file=='':
                     dialog=wx.FileDialog(None,'wxpython Notebook',style=wx.SAVE)
                     if dialog.ShowModal()==wx.ID_OK:
                            self.file=dialog.GetPath()
                            self.text.SaveFile(self.file)
                     dialog.Destroy()
              else:
                     self.text.SaveFile(self.file)
      
       def OnSaveAs(self,event):
              dialog=wx.FileDialog(None,'wxpython notebook',style=wx.SAVE)
              if dialog.ShowMoadl()==wx.ID_OK:
                     self.file=dialog.GetPath()
                     self.text.SaveFile(self.file)
              dialog.Destory()
       def OnClose(self,event):
              self.frame.Destory()
       def OnAbout(self,event):
              wx.MessageBox('A simple editor!','wxpython Notebook',wx.OK)
       def OnRClick(self,event):
              pos=(event.GetX(),event.GetY())
              self.panel.PopupMenu(self.menu.edit,pos)
       def OnUndo(self,event):
              self.text.Undo()
       def OnRedo(self,event):
              self.text.Redo()
       def OnCut(self,event):
              self.text.Cut()
       def OnCopy(self,event):
              self.text.Copy()
       def OnPaste(self,event):
              self.text.Paste()
       def OnSelectAll(self,event):
              self.text.SelectAll()
       def OnColor(self,event):
              if self.menu.view.IsChecked(1051):
                     self.text.SetBackgroundColour('black')
                     self.text.SetForegroundColour('green')
                     self.text.Refresh()
              else:
                     self.text.SetBackgroundColour('white')
                     self.text.SetBackgroundColour('black')
                     self.text.Refresh()
       def OnTrans(self,event):
              r=wx.GetNumberFromUser(u'��ѡ��͸����','','wxpython Notebook',80,min=30)
              if r!=-1:
                     self.frame.SetTransparent((r*255/100))
                     self.Refresh()
       def Resize(self,event):
              newsize=self.frame.GetSize()
              width=newsize.GetWidth()-10
              height=newsize.GetHeight()-50
              self.text.SetSize((width,height))
              self.text.Refresh()
                           
app=MyApp()
app.MainLoop()
