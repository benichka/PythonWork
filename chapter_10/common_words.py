# Take a file and count occurences of a specific text in it.
text_file = input("Choose a text file from which to count occurences of a text: ")
occurence = input("What text do you want to count in the file?: ")

try:
    with open(text_file, 'r', encoding="utf-8") as tf:
        contents = tf.read()
except:
    print("Error trying to read the file.")
else:
    occurence_count = contents.lower().count(occurence)

    print("There are " + str(occurence_count) + " occurences of the word "
            + occurence + " in the file " + text_file + ".")

