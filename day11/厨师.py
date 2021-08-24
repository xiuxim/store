

class cook:
    __name=""
    __age=0
    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.__name
    def setage(self,age):
        self.__age=age
    def getage(self):
        return self.__age

    def way(self):
        print(self.getage(),"岁的",self.getname(),"厨师正在蒸饭")
class cooking(cook):
    def method(self):
        print(self.getage(),"岁的",self.getname(),"厨师正在炒菜")

class food(cooking):

    def one(self):
        super().method()
        super().way()

f=food()
f.setname("张三")
f.setage(33)
f.one()