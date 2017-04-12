import requests


# Passing the user name and password to authorize
uid = ("admin","adm!nd42")


## Getting the data from the device 42 account

# Getting the details of all the buildings present
response=requests.request(method="get", url="https://192.168.0.148/api/1.0/buildings/", auth = uid, data = None, verify = False)
print response.text

# Getting the details of all the rooms present
response=requests.request(method="get", url="https://192.168.0.148/api/1.0/rooms/", auth = uid, data = None, verify = False)
print response.text

# Getting the details of all the racks present
response=requests.request(method="get", url="https://192.168.0.148/api/1.0/racks/", auth = uid, data = None, verify = False)
print response.text





