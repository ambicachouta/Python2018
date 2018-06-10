#!/usr/bin/python

import random

"""Returns a "random" 3 word phrase from a list of words."""

nouns = [
    'representative',
    'resist',
    'rip',
    'rub',
    'silly',
    'smile',
    'spell',
    'stretch',
    'stupid',
    'tear',
    'temporary',
    'tomorrow',
    'wake',
    'wrap',
    'yesterday',]

print (" ".join([nouns[random.randrange(0, len(nouns))] for i in range(3)]))

#range(0,1,2,3) # 3-1 = 2; 0 1 2

