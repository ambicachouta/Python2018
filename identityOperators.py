# Example : Identity operators in Python

x1 = 5
y1 = 5

x2 = 'Hello'
y2 = 'Hello'

x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(id(x1),id(y1),x1 is not y1)

# Output: True
print(id(x1),id(y1),x2 is y2)

# Output: False
print(id(x1),id(y1),x3 is y3)

