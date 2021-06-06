import requests
import re
username ='natas31'
password ='hay7aecuungiuKaezuathuk9biin0pu1'

url = 'http://%s.natas.labs.overthewire.org/' %username
session = requests.Session()

# args = { "username": "natas31", "password": ["'' or 1", 2] }

responce = requests.post(url ,auth=(username,password))
print(responce.text)
# print("password for natas 31 is : "+re.findall("<br>natas31(.*)<div id=",responce.text)[0])

