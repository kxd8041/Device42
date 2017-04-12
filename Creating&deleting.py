import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Passing the user name and password to authorize
uid = ("admin","adm!nd42")

# Passing the Details of the building to add
building = {"name" : "Elcamino-Drive-CA","address" : "84 Rac st","contact_name" : "Andrew", "contact_phone": "669546768", "notes": "Second site"}


response=requests.request(method="post", url="https://192.168.0.148/api/1.0/buildings/", auth = uid, data = building, verify = False)
print response


# Deleting the Building
id = ("1")
response=requests.request(method="delete", url="https://192.168.0.149/api/1.0/buildings/1", auth = uid, data = id , verify = False)
print response.text