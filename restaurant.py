class Restaurant():
    """ Description of a restaurant. """

    def __init__(self, restaurant_name, cuisine_type):
        """ Constructor for the restaurant. Simply construct the restaurant
        with a name and a type of cuisine. """
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        """ Print the description of the restaurant. """
        print("The name of the restaurant is " + self.restaurant_name
                + " and its cuisine type is " + self.cuisine_type + ".")

    def open_restaurant(self):
        print("Restaurant " + self.restaurant_name + " is now open.")

restaurant1 = Restaurant("Da Best Restaurant", "french")
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = Restaurant("Another great restaurant", "italian")
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3 = Restaurant("The magic pizza", "pizza")
restaurant3.describe_restaurant()
restaurant3.open_restaurant()
