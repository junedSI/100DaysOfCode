#Day_1 of prep from basics
#creating variables and assigning values 
#integer 
a = 2 
print(a)

#integer
b = 9223372036854775807
print(b)

#floating point
pi =3.14
print(pi)

#string 
name = 'John doe'
print(name)

#boolean
q = True
print(q)

#empty value or null data type
x = None
print(x)

x = None
print(type(x))

# When you use = to do an assignment operation, what's on the left of = is a name for the object on the right. Finally,
# what = does is assign the reference of the object on the right to the name on the left.
# That is:
# a_name = an_object  # "a_name" is now a name for the reference to the object "an_object"

a, b, c = 1, 2, 3
print(a, b, c)

a, b, _ = 1, 2, 3
print(a, b)


def my_function():      # This is a function definition. Note the colon (:)
      a = 2             # This line belongs to the function because it's indented
      return a          # This line also belongs to the same function
print(my_function())    # This line is OUTSIDE the function block


if a > b:         # If block starts here
    print(a)      # This is part of the if block
else:             # else must be at the same level as if
     print(b)     # This line is part of the else block

#or

if a > b:print(a)
else: print(b) 


# if x > y: y = x
# print(y)                            # IndentationError: unexpected indent
# if x > y: while y != z: y -= 1      # SyntaxError: invalid syntax


# Spaces vs. Tabs
# In short: always use 4 spaces for indentation.
def will_be_implemented_later():
    pass          #An empty block causes an IndentationError. 
                  #Use pass (a command that does nothing) when you have a block with no content:

# Integers in Python are of arbitrary sizes
a = 2
b = 100
c = 123456789
d = 38563846326424324

# float: Floating point number
# precision depends on the implementation and system architecture, for
# CPython the float datatype corresponds to a C double.
a = 2.0
b = 100.e0
c = 123456789.e1

# complex: Complex numbers
a = 2 + 1j
b = 100 + 10j
# The < , <= , > and >= operators will raise a TypeError exception when any operand is a complex number.

# Strings
# Python 3.x Version ≥ 3.0
# str: a unicode string. The type of 'hello'
# bytes: a byte string. The type of b'hello'
# Python 2.x Version ≤ 2.7
# str: a byte string. The type of 'hello'
# bytes: synonym for str
# unicode: a unicode string. The type of u'hello'


# Sequences and collections
# Python differentiates between ordered sequences and unordered collections(such as set and dict).
# strings(str, bytes, unicode) are sequences
# reversed: A reversed order of str with reversed function
a = reversed('hello')
