# Simple prompt.
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Multiline prompt.
print()

prompt = "If you tell me who you are, we can personalise the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")
