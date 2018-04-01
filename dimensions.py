dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# It is impossible to change the value of a tuple. This will return an error:
#dimensions[0] = 100

# One can iterate over a tuple:
for dimension in dimensions:
    print(dimension)

# It is not possible to modify the value of a tuple, but the tuple itself can be changed:
dimensions = (20, 10)
print(dimensions)
