user=[]
f=open(file="用户.txt",mode="r+",encoding="utf-8")

date=f.readlines()
for i in date:
    da=i.replace("\n","").split(",")
    print(da)

name=input("请输入姓名：")
passward=input("密码：")

