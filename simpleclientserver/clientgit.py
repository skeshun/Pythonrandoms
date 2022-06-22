import socket

client=socket.socket()

client.connect(("localhost",9999))

message=input("enter maessage :")
client.send(bytes(message,'ascii'))

print (client.recv(1024).decode)