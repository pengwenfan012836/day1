#!d:\table\python27\python
# -*- coding: UTF-8 -*-

from utilitya.sql_helper import ConnectMysql

class Admin:
    def __init__(self):
        self.connect = ConnectMysql()
    def getAll(self):

        recodes = self.connect.getAll()
        return recodes

    def getOne(self,id, name):
        sql = 'select * from employer where id =%s and name=%s'
        data = (id, name)
        recodes = self.connect.getOne(sql, data)
        return recodes
