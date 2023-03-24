import socket
import sys

HOST = 'localhost'
PORT = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

try:
    # make it listen for messages on port 3000
    # if the message is 'exit' then exit the program
    s.bind((HOST, PORT))
    print('Socket bind complete')
    s.listen(10)
    print('Socket now listening')
    
    while True:
        # keep listening and printing messages until the message is 'exit'
        conn, addr = s.accept()
        print('Connected with ' + addr[0] + ':' + str(addr[1]))
        while True:
            data = conn.recv(1024)
            print(data.decode('utf-8'))
            if data.decode('utf-8') == 'exit':
                break
        conn.close()
        


except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()