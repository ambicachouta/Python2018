"""*******************************************************************"""
# built-in functions
To obtain the entire list of built-in function, type:

# dir(__builtins__)

Standard types are available (basestring(), int() long() float() complex() type)

Conversion:
  
There are a few functions to convert a variable in
hexadecimal (hex()), octal (oct()) , ordinal (ord()), string (chr()) or unicode string (unichr())

Simpe Maths functions:

Simple mathematical functions are available:
max(), min(), sum(), pow(), abs(), round(), cmp(), divmod().

IO related:
The Files section shows how to manipulate files with
the file() type and and open() functions.

To retrieve a line of text from standard input you can use the
input() and raw_input() built-in functions.:

number = raw_input("Enter a number")

The dir() function and docstrings:
We can use Python’s built-in dir function:

 >>> dir(str)

"""*******************************************************************"""
8. Data Types

>>> int(45.33)
45
>>> float(34)
34.0
>>> my_string=str(1000)
>>> my_string
'1000'
>>> my_string[1]
'0'
>>> tuple("This is a string")
('T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 's', 't', 'r', 'i', 'n', 'g')
>>> list("This is a list")
['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 'l', 'i', 's', 't']
>>> chr(65)
'A'
>>> ord("A")
65
>>> ord('a')
97
>>> hex(4500)
'0x1194'
>>> oct(4500)
'0o10624'
>>> bin(42)
'0b101010'

"""*******************************************************************"""
# Reading input from keyboard :

Python 2 has two versions of input functions.

input() and raw_input().

The input() function treats received data as string if it is included
in quotes '' or "", otherwise data is treated as number

In Python 3, raw_input() function is deprecated. Further, received data is always treated as string
"""*******************************************************************"""
# In Python 2:

>>> MyName=input('python::') 
python::10                  # Entered data is treated as number
>>> MyName
10
>>> MyName=input("python::")
python::'10'                # Entered data is treated as string
>>> MyName
'10'
>>> MyName=raw_input("python::")
python::10                  # Entered data is treated as string even without ''
>>> MyName
'10'
>>> MyName=raw_input("python::")
python::'10'                # Entered data treated as string including ''
>>> MyName
"'10'"
"""*******************************************************************"""
# In Python 3 :

>>> MyName=input("Shell:")
something:10
>>> MyName
'10'
>>> MyName=input('Perl:')
something:'10'          # Entered data treated as string with or without ''
>>> MyName
"'10'"
>>> MyName=raw_input("Python:") # will result NameError
Traceback (most recent call last):
  File "", line 1, in 
  
    MyName=raw_input("Python:")
NameError: name 'raw_input' is not defined

"""*******************************************************************"""
#!/usr/bin/python

The print function :

In 2.x print is a statement and paranthess were optional.

In 3.x it's function and it uses parantheses like : print() and its mandatory.

Example:

print "Hello Python Developers" # is acceptable in Python 2

print ("Naresh IT") # in Python 3, print must be followed by ()

Note:
The print() function inserts a newline at the end by default.
In Python 2, it can be supressed by putting ',' at the end.
In Python 3, "end=' '" appends space instead of newline

Example:
print a,           # Trailing comma suppresses newline in Python 2

print(a, end=" ")  # Appends a space instead of a newline in Python 3


print("Linux")
print("Shell Scripting")
print("Perl Scripting")
print("Python Scritping/Programming")

print('Python')
print('Pandas')
print('Numpy')
print('django')

print("Unix",end="\n")
print('Bash Shell',end='\n') # By default print() function will print new line 
print("Perl CGI")
print("Python GUI")

name='Abiel'
print('1. Data Science',name,sep=":")
print(name,'2. Scientist',sep=':')
print('My Name is',name,'I am learning DevOps',sep=':')
print('My Name is',name,'I am learning DevOps',end=" ") # For below line continue from this
print('I use it for build deployment')

"""*******************************************************************"""
#!/usr/bin/python

age = int(input("Please enter your age: "))

#_0Test='10'

if age >= 18:
    print ("1. Your" + str(age) + "So collect your polling card")
    print ("Your " + str(age) + " So collect your polling card")
    print ('2. Your' + str(age) + 'So collect your polling card')
    print ('Your ' + str(age) + ' So collect your polling card')
    print ("1. Your" + str(age) + "So collect your polling card", end='\n')
    print ("1. Your" + str(age) + "So collect your polling card", sep=":")

    print ("1. Your",str(age),"So collect your polling card")
    print ('2. Your',str(age),'So collect your polling card')
    print ("1. Your",str(age),"So collect your polling card", sep=":")
    print ('2. Your',str(age),'So collect your polling card', sep=':')
    print ("1. Your",str(age),"So collect your polling card", end="\n")
    print ('2. Your',str(age),'So collect your polling card', end='\n')

else:
    print (_0Test,"Your not eligible to poll")
print ("We are out of if block")

"""*******************************************************************"""
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

"""*******************************************************************"""
print(1,2,3,4) 
print(1,2,3,4,sep='*')
print(1,2,3,4,sep='#',end='&')
"""*******************************************************************"""
# str.format() method :

Used_For="App Development"
Version=3.6

# Example 1:
# Note: Call or Access a variable using curly braces {}, are used as placeholders.

print('Python is used for {} and course is {}'.format(Used_For,Version)) 


# Example 2: 
# We can specify the order in which it is printed by using numbers (tuple index).
phone='Ipone7'
laptop="Mac Book Pro"
print('I like {0} and {1}'.format('Ipone7','Mac Book Pro'))
print('I like {1} and {0}'.format(phone,laptop))


# Example 3:
# We can use keyword arguments to format the string:

print('Hello {name}, {greeting}'.format(greeting='Goodmorning',name='John')) 

# Exmaple 4: 
# Using % operator:
x = 12.3456789
print('The value of x is %3.2f' %x)

"""*******************************************************************"""
Old: print "The answer is", 2*2
New: print("The answer is", 2*2)

Old: print x,           # Trailing comma suppresses newline
New: print(x, end=" ")  # Appends a space instead of a newline

Old: print              # Prints a newline
New: print()            # You must call the function!

Old: print >>sys.stderr, "fatal error"
New: print("fatal error", file=sys.stderr)

Old: print (x, y)       # prints repr((x, y))
New: print((x, y))      # Not the same as print(x, y)!

"""*******************************************************************"""

# This program adds two numbers

num1 = 1.5
num2 = 6.3

# Add two numbers
sum = float(num1) + float(num2)

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
