 # 没有失败的测试不能写代码
# 只写恰好使测试通过的代码
import unittest
from FizzBuzz.src.main.Calculator import Calculator
class CalculatorTest(unittest.TestCase):

    def addTest(self):
        self.assertEqual(3, self.result)

if __name__ == "__main__":
    unittest.main()
