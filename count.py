#!/usr/bin/python

str = "Welcome to python world"

sub = "o"

print(str,list(enumerate(str)))
print("")
print ("str.count(sub) : ", str.count(sub))
print("")
print ("str.count(sub) : ", str.count(sub,0,10))
print ("str.count(sub) : ", str.count(sub,0,len(str)))

print("")

sub = "python"

print(str,list(enumerate(str)))
print("")
print ("str.count(sub) : ", str.count(sub))
print ("str.count(sub) : ", str.count(sub,0,len(str)))

