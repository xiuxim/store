num=[]
sum=0
i=1
ave=0
max=0
a=0
while i<=6:
    print("请输入第",i,"科成绩")
    score=int(input())
    num.append(score)
    if max<score:
        max=score
    sum=sum+score
    i=i+1
ave=sum/6

min = num[0]
for a in num:
    if min>a:
        min=a
print("最小值为：",min)
print("最大值为：",max)
print("平均值为：",ave)
print("总分数为：",sum)
