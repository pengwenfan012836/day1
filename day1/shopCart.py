#! D:/table/python3/python

# 所有产品的信息
import time
info = {
    1: {
        'name': 'banner',
        'price': 20,
    },
    2: {
        'name': 'origin',
        'price': 30,
    },
    3: {
        'name': 'chestnut',
        'price': 50,
    }
}

print('\t\t\t\t\t\t\t欢迎来到水果商城！')
print('\t\t\t\t\t\t\t下面是所有水果，请随意选择')

# 遍历得多所有的产品
for infos in info.values():
    for keys, names in infos.items():
        print('{0}:{1}  '.format(keys,names),end='')
    print()
isxontibuy = 'y'
money = input('输入你想拥有的money：')
while isxontibuy == 'y':
    # 输入基本信息:
    fruit = input('输入水果名称：')

    for infos in info.values():
        for key, value in infos.items():
          if fruit == value:
              money =int(money) - int(infos['price'])
              print('剩余money：', money)
              isxontibuy = input('是否继续（y/n）\n')
              if isxontibuy == 'n':
                  print("欢迎下次光临,三秒后会退出！")
                  time.sleep(3)
                  break
          if isxontibuy == 'n':
              break
          print('{0}:{1}  '.format(key, value), end='')
        print()
