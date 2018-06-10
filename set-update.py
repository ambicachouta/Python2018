#6	Set Union with Mutation =		a_set.update()

# Syntax: a_set.update(an_iter)

# Example:

s = set([1, 2, 3, 4, 5])
s.update(set([5, 6, 7]))

print (s)

#Output : set([1, 2, 3, 4, 5, 6, 7])

'''Mutates a_set to be the union of set a_set and the set of 
elements in iterable an_iter. Returns None.'''
