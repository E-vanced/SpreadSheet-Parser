import pip
import setuptools
import os
import os.path 
import csv
import sys

from datetime import date

today = date.today()
print("Today's date is", today.strftime("%#m/%#d/%Y"))


# AT A LATER TIME I WOULD LIKE TO IMPLEMENT THE GOOGLE SHEETS API
# FOR NOW I AM JUST WORKING OUT THE MATH OF GETTING THE CORRECT SERIAL NUMBERS

# r"C:\Users\ELATIOLAIS\Downloads\cameras-report.csv"
# r"C:\Users\ELATIOLAIS\Downloads\Testing reports.csv"
with open(r"C:\Users\ELATIOLAIS\Downloads\Testing reports.csv" , newline='') as csvfile:
    reportReader = csv.DictReader(csvfile,)
    for row in reportReader:
        if(row['DATE'] == today.strftime("%#m/%#d/%Y")):
            print(row['DATE'], row['SERIAL NUMBER'])


# DONE ------ need to have script grab the corresponding serial number with the date
# DONE ------ if(date == today's date), then isolate all rows containing today's date
# after, grab all of the serial numbers that start with "AMC" and put them into an array
# have user input file path via drag and drop because end user accessiblity
# have ability for to user to select month, day, and year previous to current date