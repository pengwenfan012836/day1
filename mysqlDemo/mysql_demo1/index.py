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
#     这段 Python 代码看起来没有什么需要优化的地方，因为它只是简单地从数据库中获取一条记录，并根据返回结果决定是否退出程序。但是，如果您想优化一下代码，可以考虑以下几点：

# 使用更好的命名规范。根据 PEP 8 规范，变量名应该使用小写字母和下划线，函数名应该使用小写字母和下划线，并应该具有描述性。例如，可以将 isPass 改为 is_pass，maina 改为 admin_instance。

# 使用更好的异常处理。如果调用 maina.getOne(id, name) 时发生了异常，程序会崩溃并退出。可以使用 try-except 块来捕获异常并进行处理，以确保程序的健壮性。

# 使用更好的用户界面。可以考虑使用 GUI 界面或 Web 界面代替命令行界面，以提供更好的用户体验。

# 优化后的代码示例：