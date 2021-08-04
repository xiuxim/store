
num=[]
print("请输入第一条边：")
a=input()
a=int(a)
num.append(a)
print("请输入第二条边：")
b=input()
b=int(b)
num.append(b)
print("请输入第三条边：")
c=input()
c=int(c)
num.append(c)
if a==b or a==c or b==c:
    print(num,"构成等腰三角形!")
elif a==b==c:
    print(num,"构成等边三角形")
elif a*a+b*b==c*c or a*a+c*c==b*b or c*c+b*b==a*a:
    print(num,"构成直角三角形")
elif a+b>c or a+c>b or b+c>a:
    print(num,"构成普通三角形")
else:
    print(num,"不能构成三角形")



