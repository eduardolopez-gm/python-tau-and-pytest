# This is a comment
# integers
cars = 1234
CARS = 123
car_value= 123.4
#floats
pi = 3.14

# strings
type_of_cars = 'Ford'

# string formatting
print("{} belongs to {} brand.".format(cars, type_of_cars))

print("car is ", type_of_cars)

# uses index of the list in format
print("{1} belongs to {0} brand.".format(cars, type_of_cars))

# each symbol represents a type of the variable
print("There are %d cars of brand %s and costs %g"%(cars,type_of_cars,car_value))

# end string formatting


print(cars, CARS)
print(type_of_cars)

# range
print(list(range(10)))
print(list(range(2,10)))


print(list(range(1,10,2)))

print(list(range(10,0,-1)))

print(list(range(-10,-1)))

# Strings
print(id(type_of_cars)) # memory allocation of the variable

