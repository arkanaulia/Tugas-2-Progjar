import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 21))

commands = ['USER arkan\r\n', 'PASS 1234\r\n', 'RMD test2\r\n', 'QUIT\r\n']

i = 1
while i <= len(commands):
    try:
        s.send(commands[i-1].encode('utf-8'))
        msg = str(s.recv(1024).decode('utf-8'))
        if msg.__contains__('Directory deleted'):
            msg = msg.split('\r\n')[0]
            print(msg)
        # msg = msg.split('\r\n')[0].strip()
        # print(msg)
        i += 1
       
    except socket.error:
        s.close()
        break
else:
    msg = str(s.recv(4096).decode('utf-8'))        
    # print(msg.strip())      
    s.close()