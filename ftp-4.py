import socket, os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 21))

commands = ['USER arkan\r\n', 'PASS 1234\r\n', 'TYPE A\r\n', 'PASV\r\n','STOR aaa.mp4\r\n', 'QUIT\r\n']


def sendFile(pathFile, conn):
    with open(pathFile, "rb") as sf:
        data = sf.read(4096)
        while data:
            conn.sendall(data)
            # data = sf.read(1024)
            data = sf.read(4096)
            # print('Sent')
    sf.close()
    # print('Sent')

i = 1
while i <= len(commands):
    try:
        s.send(commands[i-1].encode('utf-8'))
        msg = str(s.recv(4096).decode('utf-8'))
        print(msg.strip())

        if msg.__contains__("Entering Passive Mode"):
            msg = msg.split('\r\n')[0].strip()
            ports = msg.strip().split()[-1].strip('()')
            p1, p2 = ports.split(',')[-2:]
            data_port = int(p1) * 256 + int(p2)
            
            data_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            data_sock.connect(('localhost', data_port))

            file_name = ' '.join(commands[4].strip('\r\n').split()[1:])
            path = os.path.join(os.getcwd(), file_name)
            # print(path)

            sendFile(path, data_sock)
            data_sock.close()
            msg = str(s.recv(1024).decode('utf-8'))
            print(msg.strip())
        i += 1
                
    except socket.error:
        s.close()
        break
else:       
    msg = str(s.recv(4096).decode('utf-8'))        
    print(msg.strip())      
    s.close()
