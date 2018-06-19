import wx
import wx.adv
from datetime import date

today = date.today()

class simpleapp_wx(wx.Frame):
      
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Simple App")
        panel = MainPanel(self)


class MainPanel(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent=parent)
		self.frame = parent
		self.initialize()

	def initialize(self):
		sizer = wx.GridBagSizer(vgap = 10, hgap = 10)

		self.entry = wx.TextCtrl(self,-1,value=u"Enter text here.")
		sizer.Add(self.entry,(0,0),(1,1),wx.EXPAND)

		self.date = wx.adv.DatePickerCtrl(self, -1, dt=today)
		sizer.Add(self.date, (1,0), (2, 1), wx.EXPAND)
		self.SetSizerAndFit(sizer)
		


if __name__ == "__main__":
	app = wx.App(False)
	frame = simpleapp_wx()
	frame.Show(True)
	app.MainLoop()

 # wx.adv.DatePickerCtrl
 # wx.Gauge
 # wx.ListCtrl   

 # Event handlers are methods which will be called when something happens in the GUI.
 # We bind the event handlers to specific widgets on specific events only.