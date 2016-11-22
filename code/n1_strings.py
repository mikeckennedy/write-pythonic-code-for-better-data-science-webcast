name = "Michael"
age = 43000

# print('Hello ' + name + ', you are ' + age + ' years old')
# not pythonic
print('Hello ' + name + ', you are ' + str(age) + ' years old')

print('Hello %s, you are %d years old' % (name, age))

print('Hello {}, you are {} years old'.format(name, age))
print('You are {1:,} years old {0}, right {1}'.format(name, age))

data = {'name': name, 'age': age}
print(data)

print("You are {age:,} years old {name}, right {name}".format(**data))

# Python 3.6
# print(f"You are {age} years old {name}, right {name}")
