
class computer:
    __size=0
    __price=0
    __cpu=""
    __ram=0
    __time=0

    def setsize(self,size):
        self.__size=size
    def getsize(self):
        return self.__size
    def setprice(self,price):
        self.__price=price
    def getprice(self):
        return self.__price
    def setcpu(self,cpu):
        self.__cpu=cpu
    def getcpu(self):
        return self.__cpu
    def setram(self,ram):
        self.__ram=ram
    def getram(self):
        return self.__ram
    def settime(self,time):
        self.__time=time
    def gettime(self):
        return self.__time

    def write(self,writetime):
        print("使用笔记本电脑打字，",writetime,"长时间")
    def play(self,playtime):
        print("使用笔记本电脑打游戏，", playtime, "长时间")
    def look(self,looktime):
        print("使用笔记本电脑看视频，", looktime, "长时间")
    def showcomputer(self):
        print("笔记本电脑的屏幕大小：",self.__size,"价格：",self.__price,"cpu型号：",self.__cpu,"内存大小",self.__ram,"待机时长：",self.__time)

c=computer()
c.setsize(20)
c.setprice(30000)
c.setcpu("pppp")
c.setram(256)
c.settime(5)
c.write(30)
c.play(50)
c.look(50)
c.showcomputer()

