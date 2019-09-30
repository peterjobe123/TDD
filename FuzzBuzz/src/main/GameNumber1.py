class GameNumber1:

    def isDivided(self,x, y):
        return (x % y) == 0
    def getFuzzBuzz(self, number):

        if self.isDivided(number,15):
            return "FuzzBuzz"
        if self.isDivided(number,3):
            return "Fuzz"
        if self.isDivided(number,5):
            return "Buzz"
        return str(number)


