


def cacluate(*args):
    ave=sum(args)/len(args)
    date=[]
    for i in args:
        if i>ave:
            date.append(i)
    return ave,date

print(cacluate(1,2,3,4,5,6,7,8,9))


