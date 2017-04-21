import os
import csv
import json
import logging
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)




#Getting the current working directory and checking the file which ends with .csv (Assuming only one file is present in the directory)
#write a function to
ofile=''
for file in os.listdir(os.getcwd()):
    if file.endswith(".csv"):
        ofile=file



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
response=requests.request(method="get", url="https://192.168.0.29/api/1.0/buildings/", auth = uid, data = None, verify = False)
j=json.loads(response.text)
i= j['total_count']

for each in range(i):
    availbuil.append(j['buildings'][each]['name'])

# Getting the available rooms
response=requests.request(method="get", url="https://192.168.0.29/api/1.0/rooms/", auth = uid, data = None, verify = False)
j=json.loads(response.text)
i= j['total_count']
for each in range(i):
    x= j['rooms'][each]['building'] + ":"+ j['rooms'][each]['name']
    availroom.append(x)

# Getting the available racks
response=requests.request(method="get", url="https://192.168.0.29/api/1.0/racks/", auth = uid, data = None, verify = False)
j=json.loads(response.text)
i= j['total_count']
for each in range(i):
    x= j['racks'][each]['building'] + ":"+ j['racks'][each]['room']+":"+j['racks'][each]['name']
    availrack.append(x)

print availrack
### CSV reader to read the whole csv file and print the buildings, rooms, & racks
f = open(ofile)
reader = csv.reader(f)
for row in reader:

    if row[23]!="None":
        if row[23]!="Building":
            building=row[23]
            if building in availbuil:
                pass
            else:
                buildingdata= {"name":building}
                building = {"name": building, "address": "84 Rac st", "contact_name": "Andrew",
                            "contact_phone": "669546768", "notes": "Second site"}
                response = requests.request(method="post", url="https://192.168.0.148/api/1.0/buildings/", auth=uid,
                                            data=building, verify=False)
                print response

    if row[24]!="None":
        if row[24]!="Room":
            room =(row[23]+":"+row[24])
            if room in availroom:
                pass
            else:
                buildingdata= {"name":building}

    if row[25]!="None":
        if row[25]!="Rack":
            rack =(row[23] + ":" + row[24]+":"+row[25])
            if rack in availrack:
                pass
            else:
                buildingdata = {"name": building}


