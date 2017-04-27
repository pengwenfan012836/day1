#!d:\table\python27\python
# -*- coding: UTF-8 -*-
import SocketServer

class MyServer(SocketServer.BaseRequestHandler):
    def setup(self):
        pass

    def handle(self):

        connec = self.request
        isTrue = True
        while isTrue:
          connec.send('sb')
          data = connec.recv(1024)
          if data == 'exit':
              isTrue = False
        connec.close()

    def finish(self):
        pass


if __name__ == '__main__':
    server = SocketServer.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
    server.serve_forever()