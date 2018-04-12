# Get the favorite number of a person if it exists; otherwise, ask for it and
# store it in a file.
import json

filename = "text_files/favorite_number.json"

def get_favorite_number():
    """ Main function. """
    favorite_number = retrieve_favorite_number()
    if(favorite_number):
        print("You favorite number is " + favorite_number + ".")
    else:
        favorite_number = set_favorite_number()
        print(favorite_number + " was stored as your favorite number.")

def retrieve_favorite_number():
    """
    Try to read the favorite number from the file where it is stored.
    If found, return it. If not, return none.
    """

    try:
        with open(filename, 'r', encoding="utf-8") as tf:
            favorite_number = json.load(tf)
    except FileNotFoundError:
        return None
    else:
        return favorite_number

def set_favorite_number():
    """ Prompt the user for his favorite number and store it to a file. """

    favorite_number = input("What is your favorite number?: ")
    with open(filename, 'w', encoding="utf-8") as tf:
        json.dump(favorite_number, tf, ensure_ascii=False)

    return favorite_number


get_favorite_number()
