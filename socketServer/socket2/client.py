#!d:\table\python27\python
# -*- coding: UTF-8 -*-

import socket

# 创建socket并建立连接
ip_port = ('127.0.0.1', 9999)
socket = socket.socket()

customer = socket.connect(ip_port)

while True:
    data = socket.recv(1024)
    print data
    inp = raw_input('')
    socket.sendall(inp)

    if inp == 'exit':
        break
socket.close()