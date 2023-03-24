# connect to a socket at port 3000 and prompt the user for a message
# if the message is 'exit' then exit the program

import socket

HOST = 'localhost'
PORT = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

s.connect((HOST, PORT))
print('Socket connected to ' + HOST + ' on port ' + str(PORT))

while True:
    msg = input('Enter a message: ')
    s.send(msg.encode('utf-8'))
    if msg == 'exit':
        break
        