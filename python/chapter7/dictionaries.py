# dictionary contents key / value pairs
# definition of an empty dictionary
empty_dict = {}

stuff = {
    "food": 15,
    "energy": 80,
    "health": 100,
    "enemies": 5
}

print('Dictionary')
print(stuff)
print('Dictionary keys')
print(stuff.keys())
print('Dictionary values')
print(stuff.values())

new_items = {"arrows": 10, "rocks": 3}
# Extends the existing dictionary
stuff.update(new_items)
print(stuff)

# methods
# removes the last element from the dictionary
print(stuff.popitem())
# return the value of the key that we are querying
print(stuff.get("food"))





