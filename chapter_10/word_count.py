def count_words(filename, file_encoding="utf-8"):
    """ Count the approximate number of words in a file. """

    try:
        with open(filename, encoding=file_encoding) as text_file:
            contents = text_file.read()
    except FileNotFoundError:
        #print("The file " + filename + " can not be found.")
        pass
    except UnicodeDecodeError:
        print("The encoding '" + file_encoding
                + "' does not match the file encoding.")
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words)
                + " words in it.")

filename = 'text_files/alice.txt'
count_words(filename, 'ascii')

filenames = ['text_files/little_women.txt', 'text_files/moby_dick.txt',
        'siddhartha', 'text_files/alice.txt']
for filename in filenames:
    count_words(filename, 'utf-8')
