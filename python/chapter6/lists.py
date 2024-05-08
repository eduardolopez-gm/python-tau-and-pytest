fruits = ['banana', 'cherry', 'apple']
user_data = ['Eduardo', 38, 'QA Engineer', 2000]

print(user_data)
# access an element of the list | check len of the list
print(user_data[0], len(user_data))

# add data to the list
user_data.append('single')
# add another list to the list
fruits.extend(['orange', 'pear'])
print(fruits)

# remove an element from the list

user_data.remove('QA Engineer')
print(user_data)

# delete an element from the list

del user_data[2]
print(user_data)
fruits.sort()
print(fruits)

# check if an element is in the list
print(38 in user_data)
print(user_data.count(38)>0)


