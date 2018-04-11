# Prompt someone their name and write it to a file.
guest_name = input("What's your name?: ")
with open("text_files\guest.txt", 'w') as text_file:
    text_file.write(guest_name)
