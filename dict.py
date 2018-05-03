#!/usr/bin/python
        # Key & Value
dict1 = {"C programming" : ".c",
         "C plus plus" : ".cpp-mistyped",
         "Python" : ".py",
         "one" : 1,
         2 : "two"
         }

print(dict1)

print (dict1["C plus plus"])  # Caling a specific key and it is going to print value it

# updating the existing value in dictionary
dict1["C plus plus"] = ".cpp"

print (dict1["C plus plus"])

# Adding new value in the dictionary
dict1["Ruby"] = ".rb"

print (dict1)

print(dict(enumerate(dict1)))


