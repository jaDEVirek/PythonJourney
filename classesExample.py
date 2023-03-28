# Classes



class Human:
    def __init__(self, name, age=0, weight=0):
        self.name = name
        self.age = age
        self.weight = weight


class Man(Human):

    def __init__(self, gender):
        super().__init__('')
        self.gender=gender
    def speak(self):
        print('Hello man')


tom = Man(gender='male')


tom.speak()
print(tom.name)
tom.name = 'New Name'

print(tom.name)