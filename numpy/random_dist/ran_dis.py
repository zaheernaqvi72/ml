from numpy import random as rd

# Generate a random integer from 0 to 100
x = rd.randint(100, size = (3, 5))
print(x)

# Generate a random float from 0 to 1
y = rd.choice([3, 5, 7, 9], size = (10, 2, 3))
print(y)