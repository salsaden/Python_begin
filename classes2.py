# class people has name age and gender
class people:
    def __init__(self, name, age, gender):
        self.peoplename = name
        self.peopleage = age
        self.peoplegender = gender

    def salmaa(self):
        print(self.peoplename, self.peopleage, self.peoplegender)
person1 = people("Salma", 34, "Female")
person2 = people("Erick", 42, "Male")
person3 = people("Stacy", 21, "Female")
person4 = people("Hassan", 27, "Male")
person1.salmaa()
person2.salmaa()
person3.salmaa()
person4.salmaa()
# person1.peopleage= 40
# print(person1.peopleage)
# del person1.peopleage
# print(person1.peopleage)
# class student(people):
#     pass
# x= student("Abdi", 22, "male")
# x.salmaa()
