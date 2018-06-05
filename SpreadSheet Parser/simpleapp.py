import wx
import wx.adv
from datetime import date

today = date.today()

class simpleapp_wx(wx.Frame):
      
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
        self.parent = parent
        self.initialize()

    def initialize(self):
        sizer = wx.GridBagSizer(vgap = 1, hgap = 0)

        self.entry = wx.TextCtrl(self,-1,value=u"Enter text here.")
        sizer.Add(self.entry,(0,0),(1,1),wx.EXPAND)

        self.date = wx.adv.DatePickerCtrl(self, -1, dt=today)
        sizer.Add(self.date, (1,0), (2, 1), wx.EXPAND)
        self.SetSizerAndFit(sizer)
        self.Show(True)

if __name__ == "__main__":
    app = wx.App()
    frame = simpleapp_wx(None, -1, "Simple Application")
    app.MainLoop()

 # wx.adv.DatePickerCtrl
 # wx.Gauge
 # wx.ListCtrl   