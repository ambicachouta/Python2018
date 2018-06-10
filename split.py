#!/usr/bin/python3

ruchita = "ABC123 ABC123 ABC123 ABC123 ABC123 ABC123"

print (ruchita.split())

print (ruchita.split('A'))
print (ruchita.split('123'))
print (ruchita.split('ABC'))


"""
split(str="", num=string.count(str))

	Splits string according to delimiter str (space if not provided)
	and returns list of substrings; split into at most num substrings if given.


strLower = "this@is@a@lower@case@string"

splitString = strLower.split('@')

for i in splitString:
    print (i)

print("="*30)
"""


