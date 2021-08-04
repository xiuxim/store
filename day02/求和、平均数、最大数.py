

num=[]
sum=0
i=1
max=0
while i<=10:
    print("请输入第",i,"科成绩:")
    number=input()
    number=int(number)
    num.append(number)
    if number>max:
        max=number
    sum=sum+number
    i=i+1
ave=sum/10
print("10科成绩：",num)
print("总成绩：",sum)
print("最大成绩：",max)
print("平均成绩：",ave)