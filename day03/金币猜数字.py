'''
登录系统  用户名：admin  密码：123456
'''


while True:
     name=input("请输入用户名：")
     pwd=input("请输入密码：")
     if name=="admin" and pwd=="123456":
        print("登录成功")
        break
     else:
        print("用户名或密码错误，请重新登录")

import random
num=random.randint(1,100)
count=0
integral=5000
while True:
    if integral > 0:
        guess=input("请输入要猜测的数字:")
        guess=int(guess)
        count=count+1
        if guess<num:
            integral=integral-500
            print("小了","金币剩余：",integral)
        elif guess>num:
            integral=integral-500
            print("大了","金币剩余：",integral)
        else :
            integral=integral+10000
            print("恭喜您猜对了！本次数字为：",num,"您共猜了",count,"次","金币剩余：",integral)
            print("是否继续进行游戏，是，否")
            chose=input()
            if chose=="否":
                break
            else:
                num = random.randint(1, 1000)

    else:
        print("金币不足，账户已锁定！")
        break




