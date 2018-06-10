'''
1. a_list.append  # Methods
2. a_list.extend  # Methods
3. a_list.insert  # Methods
4. a_list.remove  # Methods
5. a_list.pop  # Methods
6. a_list.reverse  # Methods
7. a_list.sort  # Methods
8. a_seq.index  # Methods
9. a_seq.count  # Methods
10. a_str.join  # Methods
'''

# 1. a_list.append  # Methods


# !/usr/bin/python

a_list = [1, 2, 3]

print(a_list, type(a_list), id(a_list))

print(list(enumerate(a_list)))

a_list.append(4)

print(a_list)

a_list.append([5, 6, 7])

print(a_list, len(a_list))

a_list.append(['Aws', 'Python'])

print(a_list)


# 2. a_list.extend  # Methods

#!/usr/bin/python

aCoolList = ["superman", "spiderman", 1947,1987,"Spiderman"]

oneMoreList = [22, 34, 56,34, 34, 78, 98]

# extending the list

# Before:
print (aCoolList)
print(type(aCoolList),len(aCoolList),id(aCoolList))
print(list(enumerate(aCoolList)))

aCoolList.extend(oneMoreList)
# After:

print (aCoolList)
print(type(aCoolList),len(aCoolList),id(aCoolList))
print(list(enumerate(aCoolList)))

"""
Extend the list by appending all the items in the given list;
equivalent to a[len(a):] = L.
"""

# 3. a_list.insert  # Methods

#!/usr/bin/python

aCoolList = ["superman", "spiderman", 1947,1987,"Spiderman"]
oneMoreList = [22, 34, 56,34, 34, 78, 98]

print (aCoolList,id(aCoolList))
print(list(enumerate(aCoolList)))
# inserting values

aCoolList.insert(0, "street750")
print (aCoolList,id(aCoolList))
print(list(enumerate(aCoolList)))

print("=======================================")

print (oneMoreList,id(oneMoreList))
print(list(enumerate(oneMoreList)))

oneMoreList.insert(5,1947)

print (oneMoreList,id(oneMoreList))
print(list(enumerate(oneMoreList)))
'''
3. list.insert(i, x) :
Insert an item at a given position. 
The first argument is the index of the element before which to insert, 
so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to
a.append(x).
'''

# 4. a_list.remove  # Methods

#!/usr/bin/python

aCoolList = ["superman", "spiderman", 1947,1987,1947,"Spiderman"]
oneMoreList = [22, 34, 56,34, 34, 78, 98]

print(aCoolList,type(aCoolList),id(aCoolList))
print(list(enumerate(aCoolList)))

aCoolList.remove('Spiderman')
print(aCoolList,type(aCoolList),id(aCoolList))
print(list(enumerate(aCoolList)))

#aCoolList.remove(2017)
#print (aCoolList)

# deleting values
aCoolList.pop(1)  # With specific index
print(aCoolList)

aCoolList.pop()   # Last element from the list
print (aCoolList)

"""
4. list.remove(x) :
Remove the first item from the list whose value is x.
It is an error if there is no such item.
"""

# 5. a_list.pop  # Methods

#!/usr/bin/python

aCoolList = ["superman", "spiderman", 1947,1987,"Spiderman"]
oneMoreList = [22, 34, 56,34, 34, 78, 98]

print(aCoolList,type(aCoolList),id(aCoolList))
print(list(enumerate(aCoolList)))
# deleting values
aCoolList.pop(1)

print(aCoolList,type(aCoolList),id(aCoolList))
print(list(enumerate(aCoolList)))

# Without index using pop method:
aCoolList.pop()

print (aCoolList)

print(aCoolList,type(aCoolList),id(aCoolList))
print(list(enumerate(aCoolList)))
'''
5. list.pop([i]) : list.pop()
Remove the item at the given position in the list, and return it. 
If no index is specified, a.pop() removes and returns the last item in the list. 
(The square brackets around the i in the method signature denote that the
parameter is optional, 
not that you should type square brackets at that position. 
You will see this notation frequently in the Python Library Reference.)
'''

# 6. a_list.reverse  # Methods

#!/usr/bin/python

aCoolList = ["superman", "spiderman", 1947,1987,"Spiderman"]
#oneMoreList = [22, 34, 56,34, 34, 78, 98]
#oneMoreList = [22, 34, 56,34, 34, 78, 98]
oneMoreList = ['1','Aws','java',' ','%','Python']
# sorting and reversing
print (oneMoreList)
oneMoreList.reverse()
print (oneMoreList)
oneMoreList.sort()
print (oneMoreList)
'''
8. list.sort(cmp=None, key=None, reverse=False):
Sort the items of the list in place (the arguments can be used for sort customization, 
see sorted() for their explanation).

9. list.reverse() :
Reverse the elements of the list, in place.
'''

# 8. a_seq.index  # Methods

#!/usr/bin/python

aCoolList = ["superman", "spiderman", 1947,1987,"Spiderman"]
oneMoreList = [22, 34, 56,34, 34, 78, 98]

# finding index
print (oneMoreList.index(34))

print (aCoolList.index(1987))

print (oneMoreList.index(30))
print (aCoolList.index(1949))

'''
6. list.index(x) :
Return the index in the list of the first item whose value is x. 
It is an error if there is no such item.
'''
# 9. a_seq.count  # Methods

#!/usr/bin/python

aCoolList = ["superman", "spiderman", 1947,1987,"Spiderman"]
oneMoreList = [22, 34, 56,34, 34, 78, 98]

# Trying to find the no.of occurenecs in a variable:

# Method : count(x)
print (aCoolList.count(1947))

print (aCoolList.count('spiderman'))

print (oneMoreList.count(34))

# Return the number of times x appears in the list.

#10. a_str.join  # Methods

#!/usr/bin/python
s = "  &  "
seq = ("a", "b", "c") # This is sequence of strings.

print(s,type(s),id(s),len(s))
print(seq,type(seq),id(seq),len(seq))

# Now, we are applying a method
print (s.join( seq ))

"""
joiner = "-"
title="10 20 30 Abc"
#title = "my first blog post"
#title = ("my", "first", "blog", "post")
strLower = "abc"

print(title)

print (joiner.join(title))
#print (len(strLower))
#print (strLower.ljust(10, '$'))
#print (strLower.rjust(10, '$'))

#print (strLower.strip('this is a '))

#print (strLower.rstrip('string'))
"""
"""
18	join(seq)
	Merges (concatenates) the string representations of elements in sequence seq into a string,
	with separator string.
"""

