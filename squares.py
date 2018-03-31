squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# Can also be written:
squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

# And also like this, with a list comprehension
squares = [value ** 2 for value in range(1, 11)]
print(squares)
