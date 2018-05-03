#!/usr/bin/python

tup1 = 3, 5, 2, 5, 6, 78, 4
tup2 = 'street', 'fatbob', 'iron883', 'night'
tup3 = "superman", 1990, "spiderman", 1992, "batman"
tup4 = ()
tup5 = (4,)

print(tup1,type(tup1),id(tup1),len(tup1))
print(tup2,type(tup2),id(tup2),len(tup2))
print(tup3,type(tup3),id(tup3),len(tup3))
print(tup4,type(tup4),id(tup4),len(tup4))
print(tup5,type(tup5),id(tup5),len(tup5))

print(tup1[3])
print(tup2[-1])
print(tup3[:3]) # End-1 : 3-1 : 2 (0,1,2)

# We are not allowed to modify the tuples

#Below line will generate error
#tup1[3] = 100

print (tup1)



