#!/usr/bin/python
"""
str1 = "Its python world....wow!!!"
str2 = "python"

print (str1.index(str2))
print (str1.index(str2, 0))
print(len(str1))
print (str1.index(str2, 0,20))

"""
str1 = "this is guido string guido example....wow!!!"
str2 = "is"

print (str1.rindex(str2))
print (str1.index(str2))

str3="guido"

print(str1.index(str3))

print(str1.rindex(str3))

"""
28	rindex(str, beg=0, end=len(string))
	Same as index(), but search backwards in string.
"""

