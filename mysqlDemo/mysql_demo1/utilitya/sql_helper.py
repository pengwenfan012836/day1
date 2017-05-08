#!d:\table\python27\python
# -*- coding: UTF-8 -*-

import MySQLdb

class ConnectMysql:
    def __init__(self):
        pass
    def getAll(self, sql, param):
        conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='pwf9410152836', db='01data')
        cur = conn.cursor()

        recodes = cur.fetchall()

        cur.close()
        conn.close()
        return recodes
    def getOne(self,sql,data):
        conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='pwf9410152836', db='01data')
        cur = conn.cursor()
        reCount = cur.execute(sql,data)
        if reCount > 0:
            recodes = cur.fetchone()
        else:
            recodes = -1
        cur.close()
        conn.close()
        return recodes