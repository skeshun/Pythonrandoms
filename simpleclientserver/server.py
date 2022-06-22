import socket

s=socket.socket()
print('socket established')
s.bind(('localhost',9999))

s.listen(3)
print('listening')



while True:
    client, addr =s.accept()
    print("connected with ", addr)

    client.send(bytes('Welcome to server Esh','ascii'))
    client.close()
