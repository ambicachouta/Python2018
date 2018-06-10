#7	Set Intersection with Mutation 	=		a_set.intersection_update()

# Syntax: a_set.intersection_update(an_iter)

# Example:

s = set([1, 2, 3, 4, 5])
s.intersection_update(set([5, 6, 7]))

print (s)

#Output : set([5])

'''Mutates a_set to be the intersection of set a_set and
the set of elements in iterable an_iter. Returns None.'''
