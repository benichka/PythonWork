# Read a file and display the whole content.
file_path = 'text_files/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# Read line by line.
print()
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

# Read all line and store them in a variable.
print()
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
