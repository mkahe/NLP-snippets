class Person:
    count = 0 # class variable
    def __init__(self, name, age):
        self.name = name # object variable
        self.age = age
        Person.count +=1
    def get_name(self):
        print('name is %s' %self.name)
    def birthday(self):
        self.age += 1
        print('happy birthday %s, your age is now %i' %(self.name, self.age))

jadi = Person('jadi', 40)
jadi.get_name()
jadi.birthday()

amir = Person('Amir', 27)

print(Person.count)