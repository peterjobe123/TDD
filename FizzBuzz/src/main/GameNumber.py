class GameNumber:
    def __init__(self, number):
        self.number = number

    def divide(self, dividedNum):
        return (self.number % dividedNum == 0)

    def getFizzBuzz(self):

        if self.divide(15):
            return "FizzBuzz"
        if self.divide(3):
            return "Fizz"
        if self.divide(5):
            return "Buzz"
        return str(self.number)

if __name__ == "__main__":
    a = GameNumber(3).getFizzBuzz()

