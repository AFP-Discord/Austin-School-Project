from time import sleep
import requests
import base64

def getmessage():
    ip = input('What is the persons IP or FQDN?: ')
    url = str('http://' + ip + ':5000/bWVzc2FnZS1jaGF0')
    req = requests.get(url=url)
    req1 = bytes.fromhex(str(req))
    print(req.content)
    print(req1)

message = input('What would you like to say?: ')
b64d = base64.b64encode(message.encode('ascii'))
hexd = bytes.hex(b64d)
