#!/usr/bin/python

_007 = "Python"

print (_007,len(_007))

print (_007.ljust(10, '*'))   # _007 = python 6  10-python 4=****

print (_007,len(_007))

"""
20	ljust(width[, fillchar])
	Returns a space-padded string with the original string
	left-justified to a total of
	width columns.
"""
str = "Python"

print(str,len(str))
print (str.rjust(10, '5'))
print (str.ljust(10, '5'))

"""
29	rjust(width,[, fillchar])
	Returns a space-padded string with the original
	string right-justified to a total of width columns.
"""

