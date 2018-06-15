# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 13 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class MainFrame
###########################################################################
class MyApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None)    ## add two lines here
        self.frame.Show(True)
        return True

class MainFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SN Search Script", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHints( wx.Size( -1,-1 ), wx.Size( 500,300 ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
        fgSizer4 = wx.FlexGridSizer( 5, 5, 10, 10 )
        fgSizer4.AddGrowableCol( 1 )
        fgSizer4.AddGrowableCol( 2 )
        fgSizer4.AddGrowableCol( 3 )
        fgSizer4.AddGrowableRow( 3 )
        fgSizer4.SetFlexibleDirection( wx.BOTH )
        fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )
        
        
        fgSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        fgSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        fgSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        fgSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        fgSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        fgSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Select Date:", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
        self.m_staticText1.Wrap( -1 )
        
        self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
        self.m_staticText1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        
        fgSizer4.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
        
        self.m_datePicker3 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.Point( -1,-1 ), wx.Size( -1,-1 ), wx.adv.DP_DEFAULT|wx.adv.DP_DROPDOWN|wx.TAB_TRAVERSAL )
        self.m_datePicker3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
        
        fgSizer4.Add( self.m_datePicker3, 0, wx.ALL, 5 )
        
        
        fgSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        fgSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        fgSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Select .CSV file:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        
        fgSizer4.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
        
        self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 300,-1 ), wx.FLP_DEFAULT_STYLE|wx.TAB_TRAVERSAL )
        fgSizer4.Add( self.m_filePicker1, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        fgSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        fgSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        fgSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Or Drag and Drop the file:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText31.Wrap( -1 )
        
        fgSizer4.Add( self.m_staticText31, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
        
        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,100 ), wx.TE_CHARWRAP|wx.TE_LEFT|wx.TE_WORDWRAP|wx.TAB_TRAVERSAL )
        self.m_textCtrl1.SetMinSize( wx.Size( 300,100 ) )
        self.m_textCtrl1.SetMaxSize( wx.Size( 300,100 ) )
        
        fgSizer4.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND|wx.FIXED_MINSIZE, 5 )
        
        
        fgSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        fgSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        fgSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer4.Add( fgSizer4, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer4 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        self.Show(True)
    

if __name__ == "__main__":
		app = MyApp()		
		app.MainLoop()
