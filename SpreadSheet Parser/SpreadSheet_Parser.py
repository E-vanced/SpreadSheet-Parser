import pip
import setuptools
import os
import os.path 
import csv
import sys

from datetime import date

# today.day, today.month, today.year
today = date.today()
print("Today's date is", today.strftime("%#m/%#d/%Y"))


# AT A LATER TIME I WOULD LIKE TO IMPLEMENT THE GOOGLE SHEETS API
# FOR NOW< I AM JUST WORKING OUT THE MATH OF GETTING TH ECORRECT SERIAL NUMBERS

# r"C:\Users\ELATIOLAIS\Downloads\cameras-report.csv"
# r"C:\Users\ELATIOLAIS\Downloads\Testing reports.csv"
with open(r"C:\Users\ELATIOLAIS\Downloads\Testing reports.csv" , newline='') as csvfile:
    reportReader = csv.DictReader(csvfile,)
    for row in reportReader:
        if(row['DATE'] == today.strftime("%#m/%#d/%Y")):
            print(row['DATE'], row['SERIAL NUMBER'])


# need to have script grab the corresponding serial number with the date
# if(date == today's date), then isolate all rows containing today's date
# after, grab all of the serial numbers that start with "AMC" and put them into an array
# determine the serial number column by matching it with the (0,SN_COLUMN)
# global variables: SN_COLUMN, CAM_SN