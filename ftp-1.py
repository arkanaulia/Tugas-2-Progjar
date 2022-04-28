import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 21))

commands = ['USER arkan\r\n', 'PASS 1234\r\n', 'QUIT\r\n']
i = 1

while i <= len(commands):
    try:
        s.send(commands[i-1].encode('utf-8'))
        msg = str(s.recv(1024).decode('utf-8'))
        # print(msg)
        if commands[i-1].__contains__('USER'):
            msg = msg.split('\r\n')[0]
            msg = msg.split('-')[1]
            print(msg)
        i += 1
                                
    except socket.error:
        s.close()
        break
else:
    msg = str(s.recv(1024))   
