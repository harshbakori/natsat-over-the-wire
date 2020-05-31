import requests
import re

username ='natas8'
password ='DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'

url = 'http://%s.natas.labs.overthewire.org/' %username

session = requests.Session()
data = {"secret":"oubWYf2kBq" , "submit":"submit"}

responce = session.post(url,data=data, auth = (username, password))
content = responce.text

# print(session.cookies['loggedin'])
print (content)

print ("password for natas9 is = " + re.findall('Access granted. The password for natas9 is (.*)',content)[0])