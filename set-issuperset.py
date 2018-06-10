# 14	Test for Superset                           =		a_set.issuperset()

# Syntax: a_set.issuperset(an_iter)

# Examples:

s = set([2, 9, 7, 1])

print(s.issuperset(s))

# Output : True

print(set([2, 9, 7, 1]).issuperset(set([1, 7])))

# Output : True

print(set([2, 9, 7, 1]).issuperset(set([1, 2, 3, 4])))

# Output : False

print(set([2, 9, 7, 1]).issuperset(set([1, 2, 3, 4, 5, 6, 7, 8, 9])))

# Output : False

print(set([2, 9, 7, 1]).issuperset([1, 2, 7, 9]))

# Output : True

'''
Returns whether the set a_set is a superset of the set of elements 
in iterable an_iter.
'''
