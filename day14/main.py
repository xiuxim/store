
from HTMLTestRunner import HTMLTestRunner
import unittest
import os

tests=unittest.defaultTestLoader.discover(os.getcwd(),pattern="addsubs.py")
runner=HTMLTestRunner.HTMLTestRunner(
    title="计算器报告",
    description="加法和减法的计算",
    verbosity=1,
    stream=open(file="计算器报告.html",mode="w+",encoding="utf-8")
)
runner.run(tests)