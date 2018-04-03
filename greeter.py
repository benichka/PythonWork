def greet_user():
    """ Display a simple greeting. """
    print("Hello!")

greet_user()

def greet_user(username):
    """ Display a simple greeting to a specific username. """
    print("Hello " + username.title() + "!")

greet_user("Benoit")
