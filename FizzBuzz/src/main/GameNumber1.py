class GameNumber1:

    def isDivided(self,x, y):
        return (x % y) == 0
    def getFuzzBuzz(self, number):

        if self.isDivided(number,15):
            return "FizzBuzz"
        if self.isDivided(number,3):
            return "Fizz"
        if self.isDivided(number,5):
            return "Buzz"
        return str(number)


