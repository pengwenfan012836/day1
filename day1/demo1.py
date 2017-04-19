#! D:/table/python3/python

# 打开一个文件


str = open('test.txt', 'r+')
n=0
while n < 3:
    n += 1
    user = input('用户名：\n')
    password = input('密码：\n')
    for test in str.readlines():
        str2 = test.strip('\n').split()
        if user in str2:
            print('存在用户')
            break
        else:
            print('重新输入')




