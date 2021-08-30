
from unittest import TestCase
from demo import calc
from ddt import ddt
from ddt import unpack
from ddt import data

da=[
    [3,4,-1],
    [3,-4,7],
    [-3,4,-7],
    [-3,-4,1],
    [0,4,-4],
    [3,0,3]
]
@ddt
class testcalcsubs(TestCase):
    @data(*da)
    @unpack
    def testsubs(self,a,b,c):
        cal=calc()
        sum=cal.subs(a,b)
        self.assertEqual(sum,c)