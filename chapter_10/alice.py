# Simple 'file not found' handling.

filename = 'text_files/alice.txt'

try:
    with open(filename, 'r', encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print("File not found. Please provide a correct path.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
