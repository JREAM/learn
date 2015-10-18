class Animal():
    def __init__(self):
        print "Animal Made"

class Piggy(Animal):
    name = "Miss"
    age = 25
    gender = "Male"
    weight = 10

    def __init__(self):
        self.gender = "Female"

    def get_name(self):
        return self.name

    @staticmethod
    def get_gender(self):
        return self.gender

    poop = property(get_name, "Hey, Sup?")

    # DO THE PROPERTY AND SETTERS!!
    @property
    def weight(self):
        return self.weight

    @weight.setter
    def weight(self, value):
        self.weight = value


p = Piggy()
print p.gender
print getattr(p, 'age')

print getattr(Piggy, 'age')
# What da hill
print Piggy.get_gender(Piggy)

setattr(p, 'color', 'red')
print p.color
print hasattr(Piggy, 'color')
print id(p)
print id(Piggy)
print isinstance(p, Piggy)
print issubclass(Animal, Piggy)
print issubclass(Piggy, Animal)
print p.poop

# p.weight(100)
# print p.weight

