# Dictionaries
# A dictionary in Python is a collection of key-value pairs.

state_capitals = {
    'Arkansas': 'Little Rock',
    'Colorado': 'Denver',
    'California': 'Sacramento',
    'Georgia': 'Atlanta'
}

my_list = [1, 2, 3]
my_set = set(my_list)

print(state_capitals)
print(my_set)
print(my_list)

first_names = {'Adam', 'Beth', 'Charlie'}

# Check membership of the set using in:
# if name in first_names:
#       print(name)

# Interactive input
name = input("What is your name? ")
# Out: What is your name? _

print(name)
# Out: Bob

x = input("Write a number:")
# Out: Write a number: 10
# x / 2
# Out: TypeError: unsupported operand type(s) for /: 'str' and 'int'
float(x) / 2
# Out: 5.0
