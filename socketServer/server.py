#!d:\table\python27\python
# -*- coding: UTF-8 -*-

import socket

# 创建socket并建立连接
socket = socket.socket()
id_linsten = ('127.0.0.1', 9999)
socket.bind(id_linsten)
socket.listen(5)

while True:
    print '实现监听'
    connec, addre =socket.accept()
    connec.send('hello')
    isTrue = True
    while isTrue:
        data = raw_input('server: ')
        connec.send(data)
        if data == 'exit':
            isTrue = False

