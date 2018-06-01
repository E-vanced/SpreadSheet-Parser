import pip
import setuptools
import os
import os.path 
import datetime
import csv
import sys


# AT A LATER TIME I WOULD LIKE TO IMPLEMENT THE GOOGLE SHEETS API
# FOR NOW< I AM JUST WORKING OUT THE MATH OF GETTING TH ECORRECT SERIAL NUMBERS

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
       
      
# need to have script grab the corresponding serial number with the date
# if(date == today's date), then isolate all rows containing today's date
# after, grab all of the serial numbers that start with "AMC" and put them into an array
# determine the serial number column by matching it with the (0,SN_COLUMN)
# global variables: SN_COLUMN, CAM_SN