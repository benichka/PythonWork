class Car():
    """ A simple attempt to represent a car. """

    def __init__(self, make, model, year):
        """ Initialise attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def read_odometer(self):
        """ Read the mileage of the car. """
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """ Update the odometer with a new value. If the value is inferior to
        the current value, an error is throw: you can't roll back an odometer.
        """
        if(mileage >= self.odometer_reading):
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self, miles):
        """ Add the miles to the existing mileage. """
        self.odometer_reading += miles

    def get_descriptive_name(self):
        """ Return a neatly formatted descriptive name. """
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

my_new_car = Car("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.update_odometer(100)
my_new_car.read_odometer()

my_new_car.update_odometer(99)
my_new_car.read_odometer()

my_new_car.increment_odometer(15)
my_new_car.read_odometer()

