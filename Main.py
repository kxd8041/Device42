import json
import csv
import requests
import configparser
import Generic
import CsvReader
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class maindevice42(object):

    def __init__(self):
        config = configparser.ConfigParser()
        config.read("info.cfg")
        self.username = config.get('client', 'uid')
        self.password = config.get('client', 'password')
        self.url = config.get('client', 'url')
        self.uid = (self.username, self.password)

    def getdetails(self):
        availbuil=[]
        availroom=[]
        availrack=[]
        building=[]
        room=[]
        rack =[]
        ## Getting the data from the device 42 account

        # Getting the details of all the buildings present
        response=Generic.G.generic("get","buildings",None)
        j=json.loads(response.text)
        i= j['total_count']

        for each in range(i):
            availbuil.append(j['buildings'][each]['name'])

        # Getting the available rooms
        response=Generic.G.generic("get","rooms",None)
        j=json.loads(response.text)
        i= j['total_count']
        for each in range(i):
            x= j['rooms'][each]['building'] + ":"+ j['rooms'][each]['name']
            availroom.append(x)

        # Getting the available racks
        response=Generic.G.generic("get","racks",None)
        j=json.loads(response.text)
        i= j['total_count']
        for each in range(i):
            x= j['racks'][each]['building'] + ":"+ j['racks'][each]['room']+":"+j['racks'][each]['name']
            availrack.append(x)

        return availbuil,availroom,availrack





    def postdetails(self,availbuil,availroom,availrack):

        file=CsvReader.c.reader()
        f = open(file)
        reader = csv.reader(f)
        for row in reader:
            if row[23]!="None":
                if row[23]!="Building":
                    building=row[23]
            if building in availbuil:
                pass
            else:
                buildingdata= {"name":building}
                response = Generic.G.generic("post", "s", "buildings", buildingdata)
                print response

            if row[24]!="None":
                if row[24]!="Room":
                    room =(row[23]+":"+row[24])
                if room in availroom:
                    pass
                else:
                    buildingdata={"name":row[24],"building":row[23]}
                    response = Generic.G.generic("post", "s", "buildings", buildingdata)

            if row[25]!="None":
                if row[25]!="Rack":
                    rack =(row[23] + ":" + row[24]+":"+row[25])
                if rack in availrack:
                    pass
                else:
                    buildingdata={"name":row[25],"building":row[23],"room":row[24]}
                    response = Generic.G.generic("post", "s", "buildings", buildingdata)


M = maindevice42()
availbuil,availroom,availrack=M.getdetails()
M.postdetails(availbuil,availroom,availrack)