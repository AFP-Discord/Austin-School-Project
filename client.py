import requests
import base64

def getmessage():
    ip = input('What is the persons IP or FQDN?: ')
    url = str('http://' + ip + ':5000/bWVzc2FnZS1jaGF0')
    req = requests.get(url=url)
    print(req.content)
    req1 = bytes.fromhex(str(req.content).strip("b'").strip("'"))
    message = base64.b64decode(req1)
    print(req.content)
    print(req1)
    print(message)
