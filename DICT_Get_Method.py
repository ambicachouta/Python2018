#!/usr/bin/python

studnet = {'Name': 'Minnu', 'Age': 7}  # Dict Variable

print ("Value :",studnet.get('Age'))

print ("Value :",studnet.get(7)) # We can not call a value

print ("Value : %s" % studnet.get('Age'))

print ("Value : %s" % studnet.get('Programming Language', "Python"))

fileName = {'Course':'Python', 'type' : 'Video', 'boolean': 1 }

sample = {1: "one", 2 : "two"}

print (fileName.get('type'))

print (fileName.keys())

print (fileName.values())

print (fileName.items())

dict_1 = {'Name': 'minnu', 'Age': 7}

print ("Value : %s" % dict_1.keys())

print ("Value : %s" % dict_1.values())