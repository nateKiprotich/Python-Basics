class User:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_user_details(self):
        print("My name is %s and I am a %s year old %s " % (self.name, self.age, self.gender))


class Fb_user(User):

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)


fb = Fb_user('Pete Scott', 46, 'Female')

fb.show_user_details()