class Animal:
    def __init__(self, name,color):
        self.name = name
        self.color =color

    def speak(self):
        raise NotImplementedError("Child classes must be implemented")


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow"

class Cow(Animal):
    def speak(self):
        return "Moo"


# create an object
dog = Dog("Tom", "\nBlack")
print(dog.name, dog.color)
print(dog.speak())

cat = Cat("\nJerry", "\nWhite")
print(cat.name,cat.color)
print(cat.speak())

cow = Cow("\nBen", "\nBrown")
print(cow.name, cow.color)
print(cow.speak())
