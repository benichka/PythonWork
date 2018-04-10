class User():
    """ A simple description of a user. """
    def __init__(self, first_name, last_name, username, email):
        """ Constructor that take a first name, last name and user information. """
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email


    def describe_user(self):
        """ Print the description of the user. """
        print("My name is " + self.first_name + " " + self.last_name + ", "
                + "my username is " + self.username + " and my email is "
                + self.email + ".")


    def greet_user(self):
        """ Personalised greeting for the user. """
        print("Hello " + self.first_name + ", how are you today?")


user1 = User("Jean-Claude", "Dusse", "jcdusse", "jdcdusse@gmail.com")
user1.greet_user()
user1.describe_user()

user2 = User("Huggy", "Les Bon Tuyaux", "hlbt", "hlbt@gmail.com")
user2.greet_user()
user2.describe_user()
