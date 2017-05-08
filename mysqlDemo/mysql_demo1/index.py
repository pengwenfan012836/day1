#!d:\table\python27\python
# -*- coding: UTF-8 -*-

import MySQLdb
from modela.admin import Admin
def main():
    maina = Admin()
    isPass = True
    while isPass:
        id = raw_input('请输入你的id')
        name = raw_input('请输入你的name')
        recode = maina.getOne(id, name)
        print recode
        if recode ==-1:
            isPass = False
        else:
            print '欢迎'

if __name__ == '__main__':
    main()