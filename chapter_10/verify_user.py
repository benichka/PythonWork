# Simple program that store the user name in a file if it's he's first logging.
# Otherwise, load the username and greet him.
# Ask the user if the last logged user is him; if not, change the stored user.
import json

filename = "text_files/verify_user.json"

def greet_user():
    """ Greet the user. """
    username = get_stored_named()
    if (username):
        is_correct_user_prompt = "Are you " + username + "?\n'y' if yes, 'n'"
        is_correct_user_prompt += " if no: "
        is_correct_user = input(is_correct_user_prompt)
        if (is_correct_user == "y"):
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

def get_stored_named():
    """ Return the stored username if it exists; otherwise return nothing. """
    try:
        with open(filename, 'r', encoding="utf-8") as tf:
            username = json.load(tf)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """ Prompt the username and store it to a file. """
    username = input("What is your name?: ")

    with open(filename, 'w', encoding="utf-8") as tf:
        json.dump(username, tf, ensure_ascii=False)

    return username


greet_user()
