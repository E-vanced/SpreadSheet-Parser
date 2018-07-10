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



sNumber = ''
fgSizer17 = None



class firstFrame(wx.Frame):
        filepath = None
        def __init__(self, parent):
                wx.Frame.__init__(self, parent, id = wx.ID_ANY, title = u"SN Search Script", pos = wx.DefaultPosition, size = wx.Size(500,500), style = wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.STAY_ON_TOP | wx.FULL_REPAINT_ON_RESIZE | wx.TAB_TRAVERSAL)

                

                self.SetSizeHints(wx.Size(-1,-1), wx.Size(-1,-1))
                self.SetExtraStyle(wx.WS_EX_VALIDATE_RECURSIVELY)
                self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
                
                bSizer4 = wx.BoxSizer(wx.VERTICAL)

                self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Instructions:\n\n1. Make sure the very first row of your spreadsheet is labeled     \n    ex: | DATE | NAME | SKU | REASON | LOCATION | SERIAL NUMBER |\n\n2. Download the Spreadsheet as .csv (Comma-separated Values)\n\n3. Select the Date corresponding to the serial numbers you want\nto check                                                                                                 \n\n4. Delete the file after usage to prevent mix-up                               \n", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
                self.m_staticText21.Wrap( -1 )
                
                bSizer4.Add( self.m_staticText21, 0, wx.ALL|wx.EXPAND, 5 )
                
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
                 
        def errorCatch(self, event, filepath):
            dlg2 = wrongFile(None)
            if filepath[-4] is not {'.csv'}:
                dlg2 = wrongFile(None)
                dlg2.ShowModal()

            else:
                pass
                


        def sendAndHide(self, event):             
            filePath = self.m_filePicker1.GetPath()
            if(filePath is ''):
                    filePath = self.m_textCtrl1.GetLineText(0)    
            errorCatch(filepath)
                
            #filePath = self.m_textCtrl1.GetLineText(0)
            datePicked = self.m_datePicker3.GetValue()
            dateFormat = datePicked.Format("%#m/%#d/%Y")                
            print(dateFormat)                               
                            
            new_frame = serialCheck(None)
            new_frame.addWidget(dateFormat, filePath)
            new_frame.Show()
        
class fileChooseDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size(-1,-1), style = wx.DEFAULT_DIALOG_STYLE | wx.STAY_ON_TOP)
        self.SetSizeHints(wx.Size(-1,-1), wx.Size(-1,-1))

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText18 = wx.StaticText(self.m_panel3, wx.ID_ANY, u"Please Select a File", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
        self.m_staticText18.Wrap(-1)

        self.m_staticText18.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))

        bSizer8.Add(self.m_staticText18, 0, wx.ALL, 20)

        self.m_button2 = wx.Button(self.m_panel3, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button2.Bind(wx.EVT_BUTTON, self.okClose)
        bSizer8.Add(self.m_button2, 0, wx.ALIGN_CENTER | wx.ALL, 5)


        self.m_panel3.SetSizer(bSizer8)
        self.m_panel3.Layout()
        bSizer8.Fit(self.m_panel3)
        bSizer3.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)


        self.SetSizer(bSizer3)
        self.Layout()
        bSizer3.Fit(self)

        self.Centre(wx.BOTH)
    def okClose(self, event):
        self.Hide()
        frame = firstFrame(None)
        frame.Show()

class chooseAgain ( wx.Dialog ):
    def __init__( self, parent ):
            wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

            self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

            bSizer10 = wx.BoxSizer( wx.VERTICAL )

            self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
            bSizer10.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )

            self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"There are no Serial Numbers containing 'AMC'\ncorresponding with this date. \n\nPlease select a different date.", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
            self.m_staticText22.Wrap( -1 )

            bSizer10.Add( self.m_staticText22, 0, wx.ALL|wx.EXPAND, 20 )

            self.m_button3 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
            self.m_button3.Bind(wx.EVT_BUTTON, self.okClose)
            bSizer10.Add( self.m_button3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


            self.SetSizer( bSizer10 )
            self.Layout()
            bSizer10.Fit( self )

            self.Centre( wx.BOTH )
            self.Bind(wx.EVT_CLOSE, self.okClose)
    def okClose(self, event):
            self.Destroy()
            frame.Show()

class wrongFile ( wx.Dialog ):
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer11.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"This is not a supported file type.", wx.DefaultPosition, wx.DefaultSize, 0 )
        
        self.m_staticText23.Wrap( -1 )

        bSizer11.Add( self.m_staticText23, 0, wx.ALL, 20 )

        self.m_button4 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button4.Bind(wx.EVT_BUTTON, self.okClose)
        bSizer11.Add( self.m_button4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()
        bSizer11.Fit( self )
        self.Bind(wx.EVT_CLOSE, self.okClose)
        self.Centre( wx.BOTH )

    def okClose(self, event):
            self.Destroy()
            frame.Show()
    
class serialCheck(wx.Frame):
        
        def __init__(self, parent):
                wx.Frame.__init__(self, parent, id = wx.ID_ANY, title = u"Serial Number Check", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP | wx.TAB_TRAVERSAL)
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
            amcRows = 0
            dlg = fileChooseDialog(None)
            dlg1 = chooseAgain(None)
            dlg2 = wrongFile(None)
            if filepath is '':
                dlg.ShowModal()
                self.Destroy()
                return          
            
            with open(filepath , newline='') as csvfile:
                reportReader = csv.DictReader(csvfile,)
                for row in reportReader:
                    if(row['DATE'] == date): #.strftime("%#m/%#d/%Y")):
                        sNumber = str(row['SERIAL NUMBER'])
                        if 'AMC' in sNumber:
                           
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
            if(amcRows is 0):
                dlg1.ShowModal()
                self.Destroy()
                return        
            #print(amcRows)
            #print(fgSizer17.GetItemCount())

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
      # the end of the widget's text
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
        