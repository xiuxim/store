
from demo import calc
from unittest import TestCase
class TestCalc(TestCase):
    def testadd1(self):
        a=3
        b=5
        c=8
        cal=calc()
        sum =cal.add(a,b)
        self.assertEqual(c,sum)
    def testadd2(self):
        a=3
        b=-5
        c=-2
        cal = calc()
        sum = cal.add(a, b)
        self.assertEqual(c, sum)
    def testadd3(self):
        a = -3
        b = -5
        c = -8
        cal = calc()
        sum = cal.add(a, b)
        self.assertEqual(c, sum)
    def testadd4(self):
        a = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        b = 5
        c = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005
        cal = calc()
        sum = cal.add(a, b)
        self.assertEqual(c, sum)