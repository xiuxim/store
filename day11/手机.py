
import time
class oldphone:
    __name=""

    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.__name

    def call(self,phone):
        print("正在给",phone,"打电话")
        for i in range(10):
            print(".",end="")
            time.sleep(1)
        print('\n')
class newphone(oldphone):
    def call(self,number):
        print("语音拨号中...")
        super().call(number)

o=oldphone()
o.setname("小米")
o.call("123456789")
n=newphone()
n.call("987654321")
print("品牌为：",o.getname(),"的手机很好用")