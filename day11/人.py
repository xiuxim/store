
class person:
    __name=""
    __age=0
    __sax=""

    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.__name
    def setage(self,age):
        self.__age=age
    def getage(self):
        return self.__age
    def setsax(self,sax):
        self.__sax=sax
    def getsax(self):
        return self.__sax

class worker(person):
    def work(self):
        print(self.getname(),"正在干活！")

class student(person):
    card=""
    def setcard(self,card):
        self.__card=card
    def getcard(self):
        return self.__card
    def study(self):
        print(self.getname(),"正在学习！")
    def sing(self):
        print(self.getname(),"正在唱歌！")

p=person()
w=worker()
w.setname("张三")
w.work()
s=student()
s.setname("李四")
s.sing()

