# Super (or) Base (or) Parent
class One:
    i, j = 11, 2

    def add(self):
        print("Addition of i and j is: ", (self.i+self.j))
        pass
    pass

#Inheriting class One with Two
# Sub (or) Derived (or) Child
class Two(One):
    a, b = 11, 2

    def sub(self):
        print("Subtraction of i and j is: ", (self.a - self.b))
        pass
    pass


obj2 = Two()
obj2.add()
obj2.sub()
print("Variables of classes One and Two: ", obj2.i, obj2.j, obj2.a,obj2.b)
