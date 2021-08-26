

from demo import calc
from unittest import TestCase
class TestCalc(TestCase):
    def testsubs1(self):
        a=2
        b=3
        c=-1
        cal=calc()
        date =cal.subs(a,b)
        self.assertEqual(c,date)
    def testsubs2(self):
        a = 3
        b = 2
        c = 1
        cal = calc()
        date = cal.subs(a, b)
        self.assertEqual(c, date)
    def testsubs3(self):
        a = -2
        b = 3
        c = -5
        cal = calc()
        date = cal.subs(a, b)
        self.assertEqual(c, date)
    def testsubs4(self):
        a = 3
        b = -2
        c = 5
        cal = calc()
        date = cal.subs(a, b)
        self.assertEqual(c, date)
    def testsubs5(self):
        a = 20000000000000000000003
        b = 3
        c = 20000000000000000000000
        cal = calc()
        date = cal.subs(a, b)
        self.assertEqual(c, date)