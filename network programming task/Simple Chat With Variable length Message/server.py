from socket import *

s = socket(AF_INET, SOCK_STREAM)
ip = '127.0.0.1'
port = 50000

s.bind((ip, port))
print(f"socket is binded to {port}")
s.listen(5)
print("Server is listening")

c, addr = s.accept()
print(f"connection received from {addr}")
while True:
    length_data = c.recv(10)
    length = int(length_data.decode('utf-8'))

    received_message = c.recv(length).decode('utf-8')
    print("Client : " + received_message)

    x = input('Server : ')
    if x == 'q':
        print('Bye')
        c.close()
        break

    message_data = x.encode('utf-8')
    message_length = str(len(message_data)).zfill(10).encode('utf-8')
    c.send(message_length)
    c.send(message_data)
c.close()