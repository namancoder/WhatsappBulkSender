


import pywhatkit
import csv
import datetime

results = []
with open("wp.csv") as csvfile:
    reader = csv.reader(csvfile) 
    for row in reader: # each row is a list
        results.append(row)

print(results)

for row in results[1:]:
    now = datetime.datetime.now()
    two_minutes_later = now + datetime.timedelta(minutes=1)
    hour = two_minutes_later.strftime("%H")
    minute = two_minutes_later.strftime("%M")
    print(row[1],row[3])
    print(hour,minute)
    pywhatkit.sendwhatmsg('+'+row[1], row[3],int(hour),int(minute))


