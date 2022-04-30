class One:
    i,j = 11,4

    def add(self):
        print("From class One, add result is: ", (self.i + self.j))
        pass
    pass

class Two(One):
    def sub(self):
        print("From class Two, sub result is: ", (self.i - self.j))
        pass
    pass

class Three(Two):
    def mul(self):
        print("From class Three, mul result is: ", (self.i * self.j))
        pass
    pass

class Four(Three):
    def div(self):
        print("From class Four, div result is: ", (self.i / self.j))
        pass
    pass

class Five(Three):
    def rem(self):
        print("From class Five, rem result is: ", (self.i % self.j))
        pass
    pass


four = Four()
five = Five()

four.add()
four.sub()
four.mul()
four.div()

print("********************")
five.add()
five.sub()
five.mul()
five.rem()
