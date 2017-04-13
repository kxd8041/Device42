import csv
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import json

# Passing the user name and password to authorize
uid = ("admin","adm!nd42")
availbuil=[]
availroom=[]
availrack=[]
building=[]
room=[]
rack =[]
## Getting the data from the device 42 account

# Getting the details of all the buildings present
response=requests.request(method="get", url="https://192.168.0.154/api/1.0/buildings/", auth = uid, data = None, verify = False)
j=json.loads(response.text)
i= j['total_count']
for each in range(i):
    availbuil.append(j['buildings'][each]['name'])

# Getting the available rooms
response=requests.request(method="get", url="https://192.168.0.154/api/1.0/rooms/", auth = uid, data = None, verify = False)
j=json.loads(response.text)
i= j['total_count']
for each in range(i):
    x= j['rooms'][each]['building'] + ": "+ j['rooms'][each]['name']
    availroom.append(x)

### CSV reader to read the whole csv file and print the buildings, rooms, & racks
f = open("deviceHard.csv")
reader = csv.reader(f)
for row in reader:
    if row[23]!="None":
        if row[23]!="Building":
            building=row[23]
            if building in availbuil:
                pass
            else:
                buildingdata= {"name":building}

    if row[24]!="None":
        if row[24]!="room":
            room =(row[24])
            if room in availroom:
                pass
            else:
                buildingdata= {"name":building}

    if row[25]!="None":
        if row[25]!="Building":
            rack=row[25]


