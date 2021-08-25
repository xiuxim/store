list=[
    [10,14,9,15],
    [7,4,8,10],
    [6,8,4,9],
    [8,51,10,23]
]
max=[list[0][0],list[1][0],list[2][0],list[3][0]]
v=0
i=0
while i<len(list):
    while v<len(list):
        if max[i]<list[i][v]:
            max[i]=list[i][v]
        v=v+1
    v=0
    i=i+1


min=[list[0][0],list[0][1],list[0][2],list[0][3]]
a=0
b=0
while a<len(list):
    while b<len(list):
        if min[a]>list[b][a]:
            min[a]=list[b][a]
        b=b+1
    b=0
    a=a+1


for j in max:
    for k in min:
        if j==k:
            print(j)


