#! D:/table/python3/python
import time

# 模糊查询
a = 1
while a > 0:
    #获取文本里卖弄的信息
    lines = open('employer.txt', 'r+', encoding='utf-8')

    #输入个人信息
    mess = input('输入信息（不少于三个字符\m）')
    messages = []
    counts = 0
    if len(mess) < 3:
        print('不符合要求，重新输入！')
        mess = input('输入信息（不少于三个字符）')
    else:
        for line in lines:
            if line.count(mess) > 0:
                messages.append(line.replace(mess,'好好好'))
                counts += line.count(mess)
        print('存在{0}条这样的信息'.format(counts))
        if len(messages) > 0:
            for i in messages:
                print(i)
    is_continue = input('是否继续？(y/n)')
    if is_continue == 'y':
        a = 1
    else:
        a = 0
else:
    timeid = [3, 2 ,1]
    for i in range(len(timeid)):
        print('%d 秒后退出'%(timeid[i]))
        time.sleep(1)
