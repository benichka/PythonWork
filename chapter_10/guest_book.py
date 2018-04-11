# Ask many user their name and write it into a file.
filename = "text_files\guest_book.txt"
guest_name = ''

while (guest_name != 'exit'):
    guest_name = input("What's your name?\nEnter 'exit' to exit: ")
    with open(filename, 'a') as text_file:
        if (guest_name != 'exit'):
            text_file.write(guest_name + "\n")

