
# Initializing dictionary 1
dict1 = {'Name':'Guido','Age':47}

# Initializing dictionary 2
dict2 = {'ID':880057}

# Initializing sequence
seq = ('Name','Age','ID')

# Using update to add dict2 values in dict1
dict1.update(dict2)

# Printing updated dictionary values
print("The updated dictionary is : ",dict1)

# Using fromkeys() to transform sequence into dictionary
dict1 = dict.fromkeys(seq,5)

# Printing new dictionary values
print("The new dictionary values are :",dict1)



