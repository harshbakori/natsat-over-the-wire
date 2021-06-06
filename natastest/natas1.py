import requests
import re

username="natas0"
password="natas0"

url = "http://%s.natas.labs.overthewire.org/" %username

responce = requests.get(url,auth=(username,password))
content = responce.text
print(content)
print (re.findall("<!--The password for natas(.*) is (.*) -->",content))

