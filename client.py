from time import sleep
import requests
import base64

ip = input('What is the persons IP or FQDN?: ')
url = str('http://' + ip + ':5000/bWVzc2FnZS1jaGF0')
changed = 1
previousnumber = 0
while True:
    req = requests.get(url=url)
    req1 = bytes.fromhex(str(req))
    print(req.content)
    sleep(2)