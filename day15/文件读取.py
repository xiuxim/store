
data=open(r"D:\Users\lxx\Desktop\python\day15\day15【异常和文件读取和写入】\任务\baidu_x_system.log",mode="r+",encoding="utf-8")
aa=data.readlines()
bb=[]
cc=[]
# print(aa)
for i in aa:
    bb.append(i.split(" - - "))
for i in range(0,len(bb)):
    cc.append(bb[i][0])
# print(cc)
dd=set(cc)
for i in dd:
    print(i,"出现了",cc.count(i),"次！")