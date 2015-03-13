# author: Jon Kruithof kruithj@mcmaster.ca
# date: Feb 24, 2015
# script purpose: To take the dates people entered things in the Learning Portfolio and
#                 calculate gaps in activity in days/minutes. Write those results to a CSV called
#                 date.csv - which can then be used to graph/chart.

import csv
import datetime

# create absolute references 

sfile = "sample.csv"
tfile = open("date.csv", "w")
group = {}

# open files

target = csv.writer(tfile,dialect='excel')

with open(sfile,'rU') as source:
        
    inread = csv.reader(source)

# iterate through file  

    for row in inread:
        
        username = row[2]
        combo_date = row[0] + " " + row[1] 
        entry_d = datetime.datetime.strptime(combo_date,"%Y-%m-%d %I:%M %p")
        
        if username in group:
            
# calculate the difference between the two dates

            difference = entry_d - group.get(username)
         #   print combo_date
            entry = [username,str(difference)]

# write the latest entry to the dictionary and write the username:difference pair to the CSV

            target.writerow(entry)
            group.update({username:entry_d}) 
            
            
        group.update({username:entry_d}) 

print "DONE"

#close the files

source.close()
tfile.close()