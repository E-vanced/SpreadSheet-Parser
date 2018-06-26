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
import sys
import pip
import setuptools
import os
import os.path 
import csv

from datetime import datetime

                
pathOfFile = str

amcRows = 0
sNumber = ''
fgSizer17 = None
#def readReport(date, filepath):
        
#        global amcRows
#        with open(filepath , newline='') as csvfile:
#                reportReader = csv.DictReader(csvfile,)
#                for row in reportReader:
#                        if(row['DATE'] == date): #.strftime("%#m/%#d/%Y")):
#                            sNumber = str(row['SERIAL NUMBER'])
#                            if 'AMC' in sNumber:
#                                amcRows += 1
#                                print(row['DATE'], sNumber)
#                onAddWidget
#                print(amcRows)

# self.m_staticText47 = wx.StaticText(self.m_panel11, wx.ID_ANY, u"MyLabel",
# wx.DefaultPosition, wx.DefaultSize, 0 | wx.NO_BORDER)
# self.m_staticText47.Wrap(-1)

# fgSizer17.Add(self.m_staticText47, 0, wx.ALL, 5)

# self.m_gauge6 = wx.Gauge(self.m_panel11, wx.ID_ANY, 100, wx.DefaultPosition,
# wx.DefaultSize, wx.GA_HORIZONTAL)
# self.m_gauge6.SetValue(0)
# fgSizer17.Add(self.m_gauge6, 0, wx.ALL, 5)


                                
                               

                                #print(row['DATE'], sNumber)
        #Adding the Static Text corresponding to 'SERIAL NUMBER'
        
                #Adding the Gauge or possibly throbber in the future


###########################################################################
## Class firstFrame
###########################################################################
class firstFrame(wx.Frame):
        
        def __init__(self, parent):
                wx.Frame.__init__(self, parent, id = wx.ID_ANY, title = u"SN Search Script", pos = wx.DefaultPosition, size = wx.Size(500,300), style = wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.STAY_ON_TOP | wx.FULL_REPAINT_ON_RESIZE | wx.TAB_TRAVERSAL)

                

                self.SetSizeHints(wx.Size(-1,-1), wx.Size(500,300))
                self.SetExtraStyle(wx.WS_EX_VALIDATE_RECURSIVELY)
                self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
                
                bSizer4 = wx.BoxSizer(wx.VERTICAL)
                
                self.m_panel7 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1,-1), wx.FULL_REPAINT_ON_RESIZE)
                fgSizer4 = wx.FlexGridSizer(6, 5, 10, 10)
                fgSizer4.AddGrowableCol(1)
                fgSizer4.AddGrowableCol(2)
                fgSizer4.AddGrowableCol(3)
                fgSizer4.AddGrowableRow(3)
                fgSizer4.SetFlexibleDirection(wx.BOTH)
                fgSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_NONE)
                
                #------ROW 0------#
                fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)                
                fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)          
                fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)              
                fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)                
                fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)
                
                #------ROW 1------#
                fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)
                
                self.m_staticText1 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"Select Date:", wx.Point(-1,-1), wx.Size(-1,-1), 0)
                self.m_staticText1.Wrap(-1)
                
                self.m_staticText1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNTEXT))
                self.m_staticText1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
                
                fgSizer4.Add(self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)
                
                self.m_datePicker3 = wx.adv.DatePickerCtrl(self.m_panel7, wx.ID_ANY, wx.DefaultDateTime, wx.Point(-1,-1), wx.Size(-1,-1), wx.adv.DP_DEFAULT | wx.adv.DP_DROPDOWN)
                self.m_datePicker3.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
                
                
                fgSizer4.Add(self.m_datePicker3, 0, wx.ALL, 5)               
                fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)               
                fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)
                
                #------ROW 2------#
                fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)
                
                self.m_staticText3 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"Select .CSV file:", wx.DefaultPosition, wx.DefaultSize, 0 | wx.TAB_TRAVERSAL)
                self.m_staticText3.Wrap(-1)
                
                fgSizer4.Add(self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)
                
                self.m_filePicker1 = wx.FilePickerCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size(300,-1), wx.FLP_DEFAULT_STYLE)
                fgSizer4.Add(self.m_filePicker1, 0, wx.ALL | wx.EXPAND, 5)
 
                fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)               
                fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)
                
                #------ROW 3------#
                fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)
                
                self.m_staticText31 = wx.StaticText(self.m_panel7, wx.ID_ANY, u"Or Drag and Drop the file:", wx.DefaultPosition, wx.DefaultSize, 0)
                self.m_staticText31.Wrap(-1)
                
                fgSizer4.Add(self.m_staticText31, 0, wx.ALIGN_RIGHT | wx.ALL, 5)
                
                self.m_textCtrl1 = wx.TextCtrl(self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300,100), wx.TE_CHARWRAP | wx.TE_LEFT | wx.TE_WORDWRAP)
                self.m_textCtrl1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
                self.m_textCtrl1.SetMinSize(wx.Size(300,100))
                self.m_textCtrl1.SetMaxSize(wx.Size(300,100))

                dt3 = FileDropTarget(self.m_textCtrl1)

                self.SetDropTarget(dt3)
                
                fgSizer4.Add(self.m_textCtrl1, 0, wx.ALL | wx.EXPAND | wx.FIXED_MINSIZE, 5)               
                fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)               
                fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)
                
                #------ROW 4------#
                fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)
                fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)
                
                ##### THIS BUTTON HIDES THE FIRST FRAME AND DISPLAYS THE DIALOG
                ##### BOX #####
                self.m_button7 = wx.Button(self.m_panel7, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
                self.m_button7.Bind(wx.EVT_BUTTON, self.sendAndHide)
                fgSizer4.Add(self.m_button7, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

                fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)

                fgSizer4.Add((0, 0), 1, wx.EXPAND, 5)
                
                #------ROW 5------#
                fgSizer4.Add((0, 0), 1, wx.EXPAND, 5) 
                self.m_panel7.SetSizer(fgSizer4)
                self.m_panel7.Layout()
                fgSizer4.Fit(self.m_panel7)
                bSizer4.Add(self.m_panel7, 1, wx.ALL | wx.EXPAND, 5)
                
                
                self.SetSizer(bSizer4)
                self.Layout()
                
                self.Centre(wx.BOTH)
                 
               
                


        def sendAndHide(self, event): 
                filePath = self.m_filePicker1.GetPath()
                if(filePath is None):
                        filePath = self.m_textCtrl1.GetLineText(0)                
                #filePath = self.m_textCtrl1.GetLineText(0)
                datePicked = self.m_datePicker3.GetValue()
                dateFormat = datePicked.Format("%#m/%#d/%Y")                
                print(dateFormat)                               
                self.Hide()                
                new_frame = serialCheck(None)
                new_frame.addWidget(dateFormat, filePath)
                new_frame.Show()
        

###########################################################################
## Class serialCheckz
###########################################################################
class serialCheck(wx.Frame):
        
        def __init__(self, parent):
                wx.Frame.__init__(self, parent, id = wx.ID_ANY, title = u"Serial Number Check", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_FRAME_STYLE| wx.STAY_ON_TOP | wx.TAB_TRAVERSAL)
                global fgSizer17
                
                #For onAddWidget
                
                self.number_of_serials = 0
             
                #self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
                
                bSizer9 = wx.BoxSizer(wx.VERTICAL)
                
                self.m_panel11 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
                fgSizer17 = wx.FlexGridSizer(0, 2, 0, 0)
                fgSizer17.SetFlexibleDirection(wx.BOTH)
                fgSizer17.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
                           
                
                self.m_panel11.Layout()                
                bSizer9.Add(self.m_panel11, 1, wx.EXPAND | wx.ALL, 5)                
                self.SetSizer(bSizer9)               
                self.Bind(wx.EVT_CLOSE, self.OnClose)                
                self.Centre(wx.BOTH)
                
     
        def addWidget(self, date, filepath):
            
            with open(filepath , newline='') as csvfile:
                reportReader = csv.DictReader(csvfile,)
                for row in reportReader:
                    if(row['DATE'] == date): #.strftime("%#m/%#d/%Y")):
                        sNumber = str(row['SERIAL NUMBER'])
                        if 'AMC' in sNumber:
                            global amcRows
                            amcRows += 1
                            label = "SN %s" % amcRows
                            name = "SN%s" % amcRows

                            #Adding Serial number as static text
                            new_text = wx.StaticText(self.m_panel11, wx.ID_ANY, label=sNumber, name=name)
                            new_text.Wrap(-1)
                            fgSizer17.Add(new_text, 0, wx.ALL, 5)
                           
                            new_gauge = wx.Gauge(self.m_panel11, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL, name="gauge %s" % amcRows)
                            new_gauge.SetValue(0)
                            fgSizer17.Add(new_gauge, 0, wx.ALL, 5)
                            print(row['DATE'], sNumber)                             
                            self.Layout()
                            self.m_panel11.SetSizerAndFit(fgSizer17)
                            self.Fit()
            
            print(amcRows)
            print(fgSizer17.GetItemCount())

        def OnClose(self,event):
                self.Destroy()
                sys.exit(0)
                frame = firstFrame(None)
                frame.Show()

class FileDropTarget(wx.FileDropTarget):
   """ This object implements Drop Target functionality for Files """
   def __init__(self, obj):
      """ Initialize the Drop Target, passing in the Object Reference to
          indicate what should receive the dropped files """
      # Initialize the wxFileDropTarget Object
      wx.FileDropTarget.__init__(self)
      # Store the Object Reference for dropped files
      self.obj = obj

   def OnDropFiles(self, x, y, filenames):

      """ Implement File Drop """
      # For Demo purposes, this function appends a list of the files dropped at
      # the end of the widget's textW
      # Move Insertion Point to the end of the widget's text
      self.obj.SetInsertionPointEnd()
      # append a list of the file names dropped
      #self.obj.WriteText("%d file(s) dropped:\n" % (len(filenames)))
      for file in filenames:
         self.obj.WriteText(file)
      
      return True

if __name__ == "__main__":
        app = wx.App(False)
        frame = firstFrame(None)
        frame.Show(True)	
        app.MainLoop()
        