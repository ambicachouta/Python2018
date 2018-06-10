# 15	Copy Set                                    =		a_set.copy()

# Syntax: a_set.copy()

# Example:

s = set([1, 2, 3, 4, 5])

t = s.copy()

print(type(s),type(t),id(s),id(t),s == t)

print(type(s),type(t),id(s),id(t),s is t)

# Output :
#True
# False

'''Makes a new set with the same elements as a_set.'''
