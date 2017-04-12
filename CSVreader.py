import csv


### CSV reader to read the whole csv file and print the buildings, rooms, & racks
f = open("deviceHard.csv")
reader = csv.reader(f)

for row in reader:
    print row[23],row[24],row[25]


