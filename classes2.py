# class people has name age and gender
class people:
    def __init__(self, name, age, gender):
        self.peoplename = name
        self.peopleage = age
        self.peoplegender = gender

    def display(self):
        print(self.peoplename, self.peopleage, self.peoplegender)
person1 = people("Salma", 34, "Female")
person2 = people("Erick", 42, "Male")
person3 = people("Stacy", 21, "Female")
person4 = people("Hassan", 27, "Male")
person1.display()
person2.display()
person3.display()
person4.display()
