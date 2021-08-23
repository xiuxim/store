
class person:
    name=""
    sex=""
    age=0
    cost=0
    brand=""
    volume=0
    size=0
    time=0
    inte=0

    def send(self,content):
        print("发送的短信内容：",content)
    def call(self,number,hour):
        cost=0
        if number is None:
            print("号码为空！")
        else:
            if self.cost<1:
                print("花费不足！")
            elif hour>0 and hour<10:
                cost=hour*1
                self.inte=self.inte+hour*15
            elif hour>10 and hour<20:
                cost = hour * 0.8
                self.inte = self.inte+hour * 39
            else:
                cost = hour * 0.65
                self.inte = self.inte+hour * 48

            print("花费：",cost,"积分为：",self.inte)
p=person()
p.inte=20
p.cost=10
p.send("你好！")
p.call("11111",25)




