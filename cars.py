cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

# Temporary sort the list
print("Temporary sorted list:")
print(sorted(cars))

print("The list hasn't change:")
print(cars)

# Sort the list
cars.sort()
print("The list is now sorted.")
print(cars)

print("And now in reverse order:")
cars.sort(reverse=True)
print(cars)

print("Lenght of list:")
print(len(cars))
