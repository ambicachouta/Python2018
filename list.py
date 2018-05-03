#!/usr/bin/python

list1 = [3, 5, 2, 5, 6, 78, 4]  # Number Data Type
list2 = ["street", "fatbob", "iron883", "night"] # String Data Type
list3 = ["superman", 1990, "spiderman", 1992, "batman"]# Number and String Data Type
list4 = ["a",10.75,89,' ','c','$']  # Strings - Numbers & Special Char

# []

#print("Accessing Variable",list1,"Checking the Data Type",type(list1),"Checking the Momory Location",id(list1),"Find the length of the variable",len(list1))
#print(list(enumerate(list1)))
"""
print(list1,type(list1),id(list1),len(list1))
print("")
print(list2,type(list2),id(list2),len(list2))
print("")
print(list3,type(list3),id(list3),len(list3))
print("")
print(list4,type(list4),id(list4),len(list4))
print("")
"""
print(list3,len(list3))

list3[1] = 'Guido Van Rossum'
print("")
print(list3,len(list3))
"""
list3[4] = "pygame"
print("")
print (list3)

print(list3)

print("")

del list3[1]

print("")

print (list3)

del list3

print(list3)
"""
"""
# comming up later
for x in list1:
    print (x)

print (list2[-1])
"""
