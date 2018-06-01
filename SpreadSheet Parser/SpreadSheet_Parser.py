import pip
import setuptools
import xlrd 
import os
import os.path 
import datetime
import csv
import sys


maxInt = sys.maxsize
decrement = True

while decrement:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/2)
        decrement = True



# Read the file
# r"C:\Users\ELATIOLAIS\Downloads\cameras-report.csv"
# r"C:\Users\ELATIOLAIS\Downloads\Testing reports.csv"
with open(r"C:\Users\ELATIOLAIS\Downloads\Testing reports.csv" , newline='') as csvfile:
       reportReader= csv.DictReader(csvfile,)
       for row in reportReader:
           print (row)
       
      
# need to have scrpt grab the correspondingserial number with the date
# determine the serial number column by matching it with the (0,SN_COLUMN)
# global variables: SN_COLUMN, CAM_SN