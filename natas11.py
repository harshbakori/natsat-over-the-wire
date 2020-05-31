import requests
import re
import urllib,base64

username ='natas11'
password ='U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'

url = 'http://%s.natas.labs.overthewire.org/' %username

session = requests.Session()
# data = {"needle":". /etc/natas_webpass/natas11 #" , "submit":"submit"}

cookies = {"data":"ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK"}
responce = session.post(url, auth = (username, password),cookies=cookies)
content = responce.text
print (content)

print ("password for natas12 is = " + re.findall('The password for natas12 is (.*)<br>',content)[0])



#################php code hear######################################

# <!DOCTYPE html>
# <html>
# <body>

# <?php 
# $default =array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

# function xor_encrypt($in,$key) {

#     $text = $in;
#     $outText = '';

#     // Iterate through each character
#     for($i=0;$i<strlen($text);$i++) {
#     $outText .= $text[$i] ^ $key[$i % strlen($key)];
#     }

#     return $outText;
# }

# $cipher = base64_decode("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D");
# $plain = json_encode($default);
# $key2 = 'qw8J';
# $mod = json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"));

# echo base64_encode(xor_encrypt($mod,$key2)); 
# ?>

# </body>
# </html>

