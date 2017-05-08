#!d:\table\python27\python
# -*- coding: UTF-8 -*-

import socket

# 创建socket并建立连接
client = socket.socket()
id_linsten = ('127.0.0.1', 9999)
client.connect(id_linsten)

while True:
    data = client.recv(1024)
    print data
    data = raw_input('client: ')
    client.send(data)
    if data == 'exit':
        break

