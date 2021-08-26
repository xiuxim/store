


from unittest import TestCase
from demo import calc
class testcalc(TestCase):
    def testmulti1(self):
        a = 2
        b = 3
        c = 6
        cal = calc()
        date = cal.multi(a, b)
        self.assertEqual(c, date)
    def testmulti2(self):
        a = -2
        b = -3
        c = 6
        cal = calc()
        date = cal.multi(a, b)
        self.assertEqual(c, date)
    def testmulti3(self):
        a = -2
        b = 3
        c = -6
        cal = calc()
        date = cal.multi(a, b)
        self.assertEqual(c, date)
    def testmulti4(self):
        a = 20000000000000000000000
        b = 30000000000000000000000
        c = 600000000000000000000000000000000000000000000
        cal = calc()
        date = cal.multi(a, b)
        self.assertEqual(c, date)