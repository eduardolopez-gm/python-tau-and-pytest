def user_info(name: str, age: int, city: str) -> None:
    """
    This function takes three arguments: name (a string), age (an integer), and city (a string).
    It prints a message to the console that includes the user's name, age, and city of residence.

    Args:
        name (str): The user's name.
        age (int): The user's age.
        city (str): The user's city of residence.

    Returns:
        None

    """
    print(f"{name} is {age} years old and is from {city} city.")


user_info("Edu", 35, "Resistencia") 

# user_info('Edu', 35)
# should display an error because needs 1 more argument

def user_info2(name, age, city='Washington'):
    print(f"{name} is {age} years old and is from {city} city")

user_info2('Edu', 35)

# *args -> allows for unlimited number of arguments to be passed
# **kwargs -> allows for unlimited keyword arguments to be passed
# without defining them ahead of time
def add(*args, **kwargs):
    print(sum(args))
add(2,3,4,5,6)
add(1,2,3,4,5,6,7,8,9,10)

