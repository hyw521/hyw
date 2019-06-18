import time
from socket import *
sockfd = socket()

sockfd.bind(('0.0.0.0',8888))
sockfd.listen(5)
while True:
    try:
        connfd,addr = sockfd.accept()
    except KeyboardInterrupt:
        print('server exit')
        break
    while True:
        time.sleep(1)
        data = connfd.recv(5)
        print(data.decode())
        if not data:
            break
        str = '你是一只大肥猪'
        time.sleep(0.1)
        n = connfd.send(str.encode())
        print('你发送的信息为:%s'%n)


    connfd.close()
sockfd.close()
