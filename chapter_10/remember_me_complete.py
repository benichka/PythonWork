# Simple program that store the user name in a file if it's he's first logging.
# Otherwise, load the username and greet him.
import json

filename = "text_files/username.json"

def greet_user():
    """ Greet the user. """
    username = get_stored_named()
    if (username):
        print("Welcome back, " + username + "!")
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
