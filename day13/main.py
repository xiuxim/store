
from HTMLTestRunner import HTMLTestRunner
import unittest
import mail

tests=unittest.defaultTestLoader.discover(r"D:\PYTHON1\python_day\day13",pattern="*test*.py")

runner=HTMLTestRunner.HTMLTestRunner(
    title="这是计算器测试报告",
    description="这是计算器的加法测试报告",
    verbosity=1,
    stream=open(file="计算器报告.html",mode="w+",encoding="utf-8")
)

runner.run(tests)
mail.send()
