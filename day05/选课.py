

chinese=['小明','小张','小黄','小杨']
math=['小黄','小李','小王','小杨','小周']
english=['小杨','小张','小吴','小冯','小周']
#1)	求选课学生总共有多少人
people_1=list(set(chinese).union(math))
people_2=list(set(people_1).union(english))
print("选课学生总共有",len(people_2),"人")

#2)	求只选了第一个学科的人的数量和对应的名字
print("选了第一个学科的人的数量:",len(chinese))
for i in chinese:
    print(i)

#3)	求只选了一门学科的学生的数量和对应的名字
aa=list(set(chinese).intersection(math))
bb=list(set(math).intersection(english))
cc=list(set(chinese).intersection(english))
student_1=list(set(people_2).difference(aa))
student_2=list(set(student_1).difference(bb))
student_3=list(set(student_2).difference(cc))

print(student_3)

