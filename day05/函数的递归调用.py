

def num(a,b):
    print(a)
    if a>=b:
        return 0
    else:
        return num(a+1,b)
num(1,150)

sum=0
def sumnum(a,b):
    global sum
    if a<=b:
        sum=sum+a
        a=a+1
        return sumnum(a,b)
    else:
        print(sum)
sumnum(1,300)
