import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 21))

commands = ['USER arkan\r\n', 'PASS 1234\r\n', 'TYPE I\r\n', 'PASV\r\n','MLSD\r\n', 'QUIT\r\n']

def list_file(data):
    list_data = data.split('\r\n')[:-1]
    for x in list_data:
        file_list = ' '.join(x.split()[1:])
        print(file_list)

i = 1
while i <= len(commands):
    try:
        s.send(commands[i-1].encode('utf-8'))
        msg = str(s.recv(4096).decode('utf-8'))
        # print(msg.strip())

        if msg.__contains__("Entering Passive Mode"):
            msg = msg.split('\r\n')[0].strip()
            
            ports = msg.strip().split()[-1].strip('()')
            p1, p2 = ports.split(',')[-2:]
            # print(p1, p2)

            	
            data_port = int(p1) * 256 + int(p2)
            
            data_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            data_sock.connect(('localhost', data_port))
            s.send(commands[i].encode('utf-8'))
            
            data = data_sock.recv(4096).decode('utf-8')
            while data:
                list_file(data)
                data = data_sock.recv(4096).decode('utf-8')
                    
        i += 1
                
    except socket.error:
        s.close()
        break
else:         
    msg = str(s.recv(4096))        
    # print(msg.strip())
    s.close()

