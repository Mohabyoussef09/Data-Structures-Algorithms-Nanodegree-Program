"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

numbers={}
for row in calls:
    if row[0] not in numbers:
        numbers[row[0]]=float(row[3])
    else:
        numbers[row[0]]+=float(row[3])
        
for row in calls:
    if row[1] not in numbers:
        numbers[row[1]]=float(row[3])
    else:
        numbers[row[1]]+=float(row[3])
        
number=''
maxDuration=-9999
for i in numbers:
    if numbers[i]>maxDuration:
        number=i
        maxDuration=numbers[i]


print("{:} spent the longest time, {:} seconds, on the phone during September 2016.".format(number,maxDuration))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

