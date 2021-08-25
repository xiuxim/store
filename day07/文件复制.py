
f=open(file="文件.txt",mode="r+",encoding="utf-8")
f1=open(file="古诗.txt",mode="w+",encoding="utf-8")

f1.write(f.read())

f.close()
f1.close()