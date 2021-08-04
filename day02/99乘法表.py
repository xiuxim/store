
i=1
while i<=9:
    k=1
    while k<=i:
        m=i*k
        print(i,"*",k,"=",m,"  ",end='')
        k=k+1
    print()
    i=i+1

print()

j=9
while j>0:
    p=1
    while p<=j:
        l=j*p
        print(j,"*",p,"=",l,"  ",end='')
        p=p+1
    print()
    j=j-1
'''
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()
'''
