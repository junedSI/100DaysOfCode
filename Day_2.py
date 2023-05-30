# Built-in Types
# Booleans
# bool: A boolean value of either True or False. Logical operations like and , or , not can be performed on booleans.
# x or y  # if x is False then y otherwise x
# x and y  # if x is False then x otherwise y
# not x  # if x is True then False, otherwise True

# tuple: An ordered collection of n values of any type(n >= 0).
a = (1, 2, 3)
b = ('a', 1, 'python', (1, 2))
# b[2] = 'something else'  # returns a TypeError

print(a)
print(b)
print(type(a))
print(type(b))

# list: An ordered collection of n values(n >= 0)
a = [1, 2, 3]
b = ['a', 1, 'python', (1, 2), [1, 2]]
b[2] = 'something else'  # allowed

print(a)
print(b)
print(type(a))
print(type(b))

# set: An unordered collection of unique values. Items must be hashable.
a = {1, 2, 'a'}

print(a)
print(type(a))

# dict: An unordered collection of unique key-value pairs
# keys must be hashable.
a = {1: 'one',
     2: 'two'}
b = {'a': [1, 2, 3],
     'b': 'a string'}

print(a)
print(b)
print(type(a))
print(type(b))

# You can also convert sequence or collection types
a = 'hello'

list(a)  # ['h', 'e', 'l', 'l', 'o']
print(a)
print(type(a))

set(a)  # {'o', 'e', 'l', 'h'}
print(a)
print(type(a))

tuple(a)  # ('h', 'e', 'l', 'l', 'o')
print(a)
print(type(a))