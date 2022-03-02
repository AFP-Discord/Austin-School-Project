import server
import client
print("""
This is an encrypted message sender.
1.) Get Message from peer
2.) Publish message for peer
""")
number = input("Which option would you like to do?: ")

if (number == "1") or (number == " 1") or (number == "1 "):
    client.getmessage()
else:
    message = input("What would yo like to send to your peer?: ")
    server.webserver(message)
