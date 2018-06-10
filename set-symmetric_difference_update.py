#9	Set Symmetric Difference with Mutation  =	a_set.symmetric_difference_update()

# Syntax: a_set.symmetric_difference_update(an_iter)

# Example:

s = set([1, 2, 3, 4, 5])
s.symmetric_difference_update(set([5, 6, 7]))
print (s)

# Output : set([1, 2, 3, 4, 6, 7])

'''Mutates a_set to be a set with all elements that are in exactly 
one of set a_set and iterable an_iter. Returns None.'''
