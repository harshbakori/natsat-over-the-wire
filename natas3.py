import requests
import re

username ='natas3'
password = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'

url = 'http://%s.natas.labs.overthewire.org/s3cr3t/users.txt' %username
responce=requests.get(url, auth = (username, password))
content = responce.text
print (content)

# print (re.findall('<!--The password for natas2 is (.*) -->',content)[0])