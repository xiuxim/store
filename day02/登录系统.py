'''
实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
'''

count=1
while count<=3:
    print("第",count,"次登录系统")
    name=input("用户名：")
    pwd=input("密码：")
    count=count+1
    if name=="root" and pwd=="admin":
        print("登录成功")
    else:
        print("用户名或密码错误")
if count>3:
    print("账户已锁定")
