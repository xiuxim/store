
class cub:
    __high=0
    __v=0
    __colour=""
    __quality=""

    def sethigh(self,high):
        self.__high=high
    def gethigh(self):
        return self.__high
    def setv(self,v):
        self.__v=v
    def getv(self):
        return self.__v
    def setcolour(self,colour):
        self.__colour=colour
    def getcolour(self):
        return self.__colour
    def setquality(self,quality):
        self.__quality=quality
    def getquality(self):
        return self.__quality

    def deposit(self):
        print("这个水杯的高度为：",self.__high,"容积为：",self.__v,"颜色为：",self.__colour,"材质为：",self.__quality)
c=cub()
c.sethigh(30)
c.setv(50)
c.setcolour("蓝色")
c.setquality("玻璃")
print(c.gethigh(),c.getv(),c.getcolour(),c.getquality())
c.deposit()