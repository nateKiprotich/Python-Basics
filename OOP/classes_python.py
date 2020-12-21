class Person:
    # Class Variables
    gender = 'Male'

    def __init__(self, name, age=18):
        # Instance variables
        self.name = name
        self.age = age

    def show_name(self):
        print('My name is %s and I am %s years old' % (self.name, self.age) )


p = Person("Nate", 56)
p.show_name()

print(p.gender)

p = Person(age=30, name="Nate")
p.show_name()


p = Person("Nate")
p.show_name()