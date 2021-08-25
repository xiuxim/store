'''
模式：
    r、w、rb(图片、MP3、mp4),a(附加)，+可读可写
'''

#打开（可读可写）
f=open(file="D:\PYTHON1\python_day\day07\文件.txt",mode="r+",encoding="utf-8")
#写
# f.write("鹅鹅鹅1")
# f.write("鹅鹅鹅2")
# f.write("鹅鹅鹅3")
#读
print(f.readline()) #读一行
print(f.readline())         #读两行
print(f.readlines(2))#读指定的一行i

f.close()