#!/usr/bin/python

seq = ('name', 'age', 'Gender') # A Tuple Variable

dict1 = dict.fromkeys(seq)  # Calling a Tuple Variable part of dict.fromkeys method

print ("New dictionary : %s" % str(dict1))

dict2 = dict.fromkeys(seq,10) # Assigning values to Keys

print ("New dictionary : %s" % str(dict2))

fromkeys(seq,value) : This method is used to declare a new dictionary from the sequence
mentiond in its arguments.

This function/method can also initialize the declared disctionary with "value" argument.
