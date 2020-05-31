import requests
import re

username ='natas19'
password ='4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'

url = 'http://%s.natas.labs.overthewire.org/' %username
session = requests.Session()
responce = session.get(url,auth=(username,password))
content = responce.text
print(content)