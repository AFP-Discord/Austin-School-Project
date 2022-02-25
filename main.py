from encodings import utf_8
import server
import base64
message = input('What would you like to say?: ')
b64d = base64.b64encode(message.encode('ascii'))
hexd = bytes.hex(b64d)

server.webserver(hexd)