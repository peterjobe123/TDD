import unittest
# from src.main.GameNumber1 import GameNumber1

class GameNumberTest1(unittest.TestCase):
    def testDivideBy1(self):
        self.assertEqual(GameNumber1().getFuzzBuzz(1), "1")

    def testDivideBy3(self):
        self.assertEqual(GameNumber1().getFuzzBuzz(3), "Fuzz")

    def testDivideBy5(self):
        self.assertEqual(GameNumber1().getFuzzBuzz(5), "Buzz")

    def testDivideBy15(self):
        self.assertEqual(GameNumber1().getFuzzBuzz(15), "FuzzBuzz")


suite = unittest.defaultTestLoader.loadTestsFromTestCase(GameNumberTest1)
unittest.TextTestRunner().run(suite)