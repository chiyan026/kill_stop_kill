
from socket import *

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(("127.0.0.1",8080))
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connection from', addr)
    try:
        data = tcpCliSock.recv(1024)
        print(data)
        filename = data.split()[1]
        print(filename[1:])
        f = open(filename[1:])
        outputdata = f.read()
        header = 'HTTP/1.1 200 OK\r\n\r\n'
        tcpCliSock.send(header.encode())
        for i in range(0, len(outputdata)):
            tcpCliSock.send(outputdata[i].encode())
        tcpCliSock.close()
    except IOError:
        header = 'HTTP/1.1 404 NOT FOUND\r\n\r\n'
        tcpCliSock.send(header.encode())
        tcpCliSock.close()
tcpSerSock.close()