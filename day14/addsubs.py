
from testadd import testcalcadd
from testsubs import testcalcsubs
from threading import Thread
class testcalc(Thread):
    def add(self) -> None:
        testcalcadd()

    def subs(self) -> None:
        testcalcsubs()


c=testcalc()
d=testcalc()
c.add()
d.subs()
c.start()
d.start()