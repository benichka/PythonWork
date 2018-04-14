# Simple class that displays a city name and location.
def get_city_description(name, country_name=""):
    """ Return the description of a city, with or without location. """
    if(country_name):
        result = name + ", " + country_name
    else:
        result = name

    return result.title()
