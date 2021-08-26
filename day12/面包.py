
import time
from threading import Thread
bread=0
class cook(Thread):
    username = ""
    count=0
    def run(self) -> None:
        global bread
        while True:
            if bread <500:
                bread = bread+1
                self.count=self.count+1
                print(self.username, "总共做了", self.count, "个")
            elif bread==500:
                time.sleep(2)

class buy(Thread):
    username = ""
    count = 0
    def run(self) -> None:
        money=300
        global bread
        while True:
            if money>0:
                bread=bread-1
                money=money-3
                self.count=self.count+1
                print(self.username, "总共买了", self.count, "个")
            else:
                print("金钱不足！")
                break



c1=cook()
c2=cook()
c3=cook()
c1.username="张三"
c2.username="李四"
c3.username="王五"
c1.start()
c2.start()
c3.start()

b1=buy()
b2=buy()
b3=buy()
b4=buy()
b5=buy()
b6=buy()
b1.username="一号"
b2.username="二号"
b3.username="三号"
b1.username="四号"
b2.username="五号"
b3.username="六号"
b1.start()
b2.start()
b3.start()
b4.start()
b5.start()
b6.start()