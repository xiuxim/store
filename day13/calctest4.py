
from unittest import TestCase
from demo import calc
class testcalc(TestCase):
    def testdevision1(self):
        a = 6
        b = 3
        c = 2
        cal = calc()
        date = cal.devision(a, b)
        self.assertEqual(c,date)
    def testdevision2(self):
        a = 6
        b = -3
        c = -2
        cal = calc()
        date = cal.devision(a, b)
        self.assertEqual(c, date)
    def testdevision3(self):
        a = -6
        b = 3
        c = -2
        cal = calc()
        date = cal.devision(a, b)
        self.assertEqual(c, date)
    def testdevision4(self):
        a = -6
        b = -3
        c = 2
        cal = calc()
        date = cal.devision(a, b)
        self.assertEqual(c, date)
    def testdevision5(self):
        a = 600000000000000000000000000000000000000000000
        b = 20000000000000000000000
        c = 30000000000000000000000
        cal = calc()
        date = cal.devision(a, b)
        self.assertEqual(c, date)