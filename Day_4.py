from array import *
from enum import Enum
import datetime
# Built in Modules and Functions
# Built_ins=[
#  'ArithmeticError',
#  'AssertionError',
#  'AttributeError',
#  'BaseException',
#  'BufferError',
#  'BytesWarning',
#  'DeprecationWarning',
#  'EOFError',
#  'Ellipsis',
#  'EnvironmentError',
#  'Exception',
#  'False',
#  'FloatingPointError',
#  'FutureWarning',
#  'GeneratorExit',
#  'IOError',
#  'ImportError',
#  'ImportWarning',
#  'IndentationError',
#  'IndexError',
#  'KeyError',
#  'KeyboardInterrupt',
#  'LookupError',
#  'MemoryError',
#  'NameError',
#  'None',
#  'NotImplemented',
#  'NotImplementedError',
#  'OSError',
#  'OverflowError',
#  'PendingDeprecationWarning',
#  'ReferenceError',
#  'RuntimeError',
#  'RuntimeWarning',
#  'StandardError',
#  'StopIteration',
#  'SyntaxError',
#  'SyntaxWarning',
#  'SystemError',
#  'SystemExit',
#  'TabError',
#  'True',
#  'TypeError',
#  'UnboundLocalError',
#  'UnicodeDecodeError',
#  'UnicodeEncodeError',
#  'UnicodeError',
#  'UnicodeTranslateError',
#  'UnicodeWarning',
#  'UserWarning',
#  'ValueError',
#  'Warning',
#  'ZeroDivisionError',
#  '__debug__',
#  '__doc__',
#  '__import__',
#  '__name__',
#  '__package__',
#  'abs',
#  'all',
#  'any',
#  'apply',
#  'basestring',
#  'bin',
#  'bool',
#  'buffer',
#  'bytearray',
#  'bytes',
#  'callable',
#  'chr',
#  'classmethod',
#  'cmp',
#  'coerce',
#  'compile',
#  'complex',
#  'copyright',
#  'credits',
#  'delattr',
#  'dict',
#  'dir',
#  'divmod',
#  'enumerate',
#  'eval',
#  'execfile',
#  'exit',
#  'file',
#  'filter',
#  'float',
#  'format',
#  'frozenset',
#  'getattr',
#  'globals',
#  'hasattr',
#  'hash',
#  'help',
#  'hex',
#  'id',
#  'input',
#  'int',
#  'intern',
#  'isinstance',
#  'issubclass',
#  'iter',
#  'len',
#  'license',
#  'list',
#  'locals',
#  'long',
#  'map',
#  'max',
#  'memoryview',
#  'min',
#  'next',
#  'object',
#  'oct',
#  'open',
#  'ord',
#     'pow',
#  'print',
#  'property',
#  'quit',
#  'range',
#  'raw_input',
#  'reduce',
#  'reload',
#  'repr',
#  'reversed',
#  'round',
#  'set',
#  'setattr',
#  'slice',
#  'sorted',
#  'staticmethod',
#  'str',
#  'sum',
#  'super',
#  'tuple',
#  'type',
#  'unichr',
#  'unicode',
#  'vars',
#  'xrange',
#  'zip'
# ]
# help(max)


# def sayHello():
#  """This is the function docstring."""
#  return 'Hello World'


# String function - str() and repr()
# repr(x) calls x.__repr__(): a representation of x. eval will usually convert the result of this function back to the
# original object.
# str(x) calls x.__str__(): a human-readable string that describes the object. This may elide some technical detail.

# Example 1


s = """W'o"o"""
repr(s)
str(s)

# eval(str(s)) == s  # Gives a SyntaxError
# print(eval(repr(s))) == s  # Output: True

# Example 2:
today = datetime.datetime.now()
str(today)  # Output: '2016-09-15 06:58:46.915000'
repr(today) # Output: 'datetime.datetime(2016, 9, 15, 6, 58, 46, 915000)'

print(str(today))
print(repr(today)) 

# Installing a package is as simple as typing (in a terminal / command-prompt, not in the Python interpreter)
# $ pip install[package_name]  # latest version of the package
# $ pip install[package_name] == x.x.x  # specific version of the package
# $ pip install '[package_name]>=x.x.x'  # minimum version of the package
# where x.x.x is the version number of the package you want to install.


def hello():
 """Say hello to your friends."""
 print("Hello my friends!")


hello()


def hello(name, language="en"):
 """Say hello to a person.
 Arguments:
 name: the name of the person
 language: the language in which the person should be greeted
 """
 print(name)


hello("tejashri")


class Color(Enum):
 red = 1
 green = 2
 blue = 3


print(Color.red)  # Color.red
print(Color(1))  # Color.red
print(Color['red'])  # Color.red'


a = {1, 2, 3, 4}
b = {1, 2, 3, 56, 65}
print(a.intersection(b))
print(a.union(b))
print(a.difference(b))
print(a.symmetric_difference(b))
print(a.issuperset(b))
print(a.isdisjoint(b))

print(1 in a)

restaurants = ["McDonald's", "Burger King", "McDonald's", "Chicken Chicken"]
unique_restaurants = set(restaurants)
print(unique_restaurants)


x = 'Hi'


def read_x():
 print(x)  # x is just referenced, therefore assumed global


read_x()  # prints Hi
y = 4.5


def read_y():
 print(y)  # here y is just referenced, therefore assumed global


read_y()


x = 5
print(x)  # out: 5
del x
print(x)


x = 5
print(x)  # out: 5
del x
print(x)

number = 5
if number > 2:
 print("Number is bigger than 2.")
elif number < 2:  # Optional clause (you can have multiple elifs)
 print("Number is smaller than 2.")
else:  # Optional clause (you can only have one else)
 print("Number is 2.")

a = 10
while True:
 a = a-1
 print(a)
 if a < 7:
   break
print('Done.')


my_array = array('i', [1, 2, 3, 4, 5])
print(my_array[1])
# 2
print(my_array[2])
# 3
print(my_array[0])
