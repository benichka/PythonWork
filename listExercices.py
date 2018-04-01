print("Counting to 20:")
for value in range(1, 21):
    print(str(value))

print("List of odd numbers:")
for value in range(1, 21, 2):
    print(str(value))

print("Multiples of 3:")
multiples = list(range(3, 31, 3))
print(multiples)

print("Cubes:")
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)
