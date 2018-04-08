def greet_users(names):
    """ Print a simple greeting for each name in the input list. """
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'bob']
greet_users(usernames)
