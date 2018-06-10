# 13	Test for Subset                             =		a_set.issubset()
# Syntax: a_set.issubset(an_iter)
# Examples:

s = set([2, 9, 7, 1])
print(s.issubset(s))

#Output : True

print(set([2, 9, 7, 1]).issubset(set([1, 7])))

# Output : False

print(set([2, 9, 7, 1]).issubset(set([1, 2, 3, 4])))

# Output : False

print(set([2, 9, 7, 1]).issubset(set([1, 2, 3, 4, 5, 6, 7, 8, 9])))

# Output : True

print(set([2, 9, 7, 1]).issubset([1, 2, 7, 9]))

# Output : True

'''Returns whether the set a_set is a subset of the set of 
elements in iterable an_iter.'''
