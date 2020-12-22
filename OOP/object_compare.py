class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age


p1 = Person('Pete', 34)
p2 = Person('Jane', 34)

print(p1 == p2)
