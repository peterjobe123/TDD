import unittest
from src.main.GameNumber import GameNumber

class GameNumberTest(unittest.TestCase):
    def setUp(self):
        pass

    def testDivideBy1(self):
        self.assertEqual(GameNumber(1).getFizzBuzz(),"1")

    def testDivideBy3(self):
        self.assertEqual(GameNumber(3).getFizzBuzz(),"Fizz")

    def testDivedeBy5(self):
        self.assertEqual( GameNumber(5).getFizzBuzz(),"Buzz")

    def testDivedeBy5(self):
        self.assertEqual(GameNumber(15).getFizzBuzz(), "FizzBuzz")

# if __name__ == '__main__':
# suite = unittest.defaultTestLoader.loadTestsFromTestCase(GameNumberTest)
# unittest.TextTestRunner().run(suite)