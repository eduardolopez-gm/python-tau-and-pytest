class Person:
    def __init__(self, first_name, last_name, age):
        # attributes of the class
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def initials(self):
        return f'{self.first_name[0]}.{self.last_name[0]}'
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old'

# Create a new class that inheritance some attributes from the current class
class Student(Person):
    def __init__(self, first_name, last_name, age, school):
        super().__init__(first_name, last_name, age)
        self.school = school


person1 = Person('Eduardo', 'Lopez', 35)

student1 = Student('tito', 'pence', 15, 'harvard')

print(person1.full_name(), person1.initials(), person1.__str__())

print(student1.full_name(), student1.initials(), student1.__str__())



