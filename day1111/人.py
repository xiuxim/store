
class people:
    name=""
    age=0
    weight=0
    eat=""

    def setpeople(self):
        print(self.age,"岁的",self.name,"体重是：",self.weight,"爱吃：",self.eat)

p=people()
p.name="张三"
p.age=33
p.weight=44
p.eat="饭"
p.setpeople()
