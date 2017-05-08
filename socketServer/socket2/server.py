#!d:\table\python27\python
# -*- coding: UTF-8 -*-

import socket
ip_port = ('127.0.0.1',9999)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print 'waiting....'
    conn, addr = sk.accept()
    conn.sendall('欢迎致电！')
    Flage = True
    while Flage:
        data = conn.recv(1024)
        print data
        if data == 'exit':
            Flage =False
        elif data == '0':
            conn.sendall('通过可能会被录音.balabala一大推')
        else:
            conn.sendall('请重新输入')
    conn.close()
