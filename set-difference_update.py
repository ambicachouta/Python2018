#8	Set Difference with Mutation 	=		a_set.difference_update()

# Syntax: a_set.difference_update(an_iter)

# Example:

s = set([1, 2, 3, 4, 5])
s.difference_update(set([4, 5, 6, 7]))
print (s)

# Output : set([1, 2, 3, 4])

'''Mutates a_set to be the set difference of set a_set and the 
set of elements in iterable an_iter. Returns None.'''

