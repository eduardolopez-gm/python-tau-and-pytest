

class Person: 
    # __init__method is called by the class constructor when the class is instantiated
    # and initialized properly with the arguments passed to the constructor.
    def __init__(self, first_name=None, last_name=None, age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    # self is used to reference the object that is constructed by the init method.
    # is a self reference variable

    def full_name(self):
        print('Hello {} {}'.format(self.first_name, self.last_name))

    def get_age(self):
        return self.age

person1 = Person('John' , 'Doe', 20)
person1.full_name()
print(person1.get_age())


