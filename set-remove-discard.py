# 11	Remove Specified Element from Set   = a_set.remove(), a_set.discard()

# Syntax:
#a_set.remove(x)
#a_set.discard(x)

# Example:

s = set([1, 2, 3, 4, 5])
s.remove(5)
print (s)

s.discard(7)
print (s)

s.discard(3)
print (s)

#Output:
#set([1, 2, 3, 4])
#set([1, 2, 3, 4])
#set([1, 2, 4])

'''
Removes element x from set a_set. 
If element x is not in a_set, a_set.remove raises an error, 
while a_set.discard does not. 
Returns None.
'''
