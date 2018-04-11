# Ask people why they love programming and store their reason to a file.
reasons = []
filename = "text_files/reasons.txt"

text = "Would you like to enter another reason?\n"
text += "Enter 'y' to continue, 'n' otherwise: "
while (True):
    reason = input("Reason?: ")
    reasons.append(reason)

    result = input(text)
    if (result != 'y'):
        break

with open(filename, 'a') as text_file:
    for element in reasons:
        text_file.write(element + "\n")
