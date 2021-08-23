
class student:
    __name=""
    __age=0

    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.__name
    def setage(self,age):
        if age>100 and age<0:
            print("输入非法！")
        else:
            self.__age=age
    def getage(self):
        return self.__age

    def show(self):
        print("大家好，我叫",self.__name,"，今年",self.__age,"岁了！")
    def compare(self,student):
        if student.getage() > self.__age:
            print("我比同桌大",(student.getage()-self.__age),"岁！")
        elif student.getage() < self.__age:
            print("我比同桌小",(self.__age-student.getage()),"岁！")
        else:
            print("我和同桌一样大！")

s=student()
s.setname("张三")
s.setage(25)
s.show()

s1=student()
s1.setname("李四")
s1.setage(24)
s1.show()
s.compare(s1)



