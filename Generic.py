import requests
import configparser
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Genericdata(object):

    def __init__(self):
        config = configparser.ConfigParser()
        config.read("info.cfg")
        self.username = config.get('client', 'uid')
        self.password = config.get('client', 'password')
        self.url = config.get('client','url')
        self.uid =(self.username,self.password)


    def generic(self, methodsel,device,info):

        # Generic Function to perform GET,POST, DELETE

        response=requests.request(method=methodsel, url=self.url+"/api/1.0/"+device+"/", auth = self.uid , data = info, verify = False)
        return response




G=Genericdata()
G.generic(methodsel="get",device="rooms",info= None)

