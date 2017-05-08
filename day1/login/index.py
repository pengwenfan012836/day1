#! D:/table/python3/python


# 用户登录验证
n = 0
while n < 2:

    b = 0
    user = input('用户名：')
    password = input('密码：')

    files2 = open('lockUser.txt', 'r+', encoding='utf-8')
    files = open('test.txt', 'r+',encoding='UTF-8')
    lines2 = files2.readlines()
    lines = files.readlines()

    # 判断用户是不是说锁定的那个用户
    for line in lines2:
        list2 = line.strip('\n').split()
        if user in list2:
            print('非法用户')
            b = 1
    if b == 1:
        break
    a = 0
    for line in lines:
        lis1 = line.strip('\n').split(' ');
        if lis1[0] == user and lis1[1] == password:
            a = 1
            print('用户名：{0} 密码：{1}'.format(lis1[0],lis1[1]))
            print('登录成功！')
            n = 4
    if a == 0:
        print('请重新登录')

    n = n + 1
    if n == 2:
        files2 = open('lockUser.txt', 'w+', encoding='utf-8')
        files2.write(user)


    files.close()
    files2.close()

