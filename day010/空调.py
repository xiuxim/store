
class air:
    __brand=""
    __price=0

    def setbrand(self,brand):
        self.__brand=brand
    def getbrand(self):
        return self.__brand
    def setprice(self,price):
        self.__price=price
    def getprice(self):
        return self.__price

    def open(self):
        print("空调开机了!")
    def up(self,time):
        print("空调将在",time,"分钟后自动关闭!")

a=air()
a.setbrand("格力")
a.setprice(3000)
print("空调的品牌：",a.getbrand(),"价格：",a.getprice())
a.open()
a.up(30)
