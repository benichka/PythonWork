import unittest
from city_functions import get_city_description

class TestCityFunctions(unittest.TestCase):
    """ Tests for city_functions. """

    def test_get_city_name(self):
        """ Test if the user input only the city name. """
        description = get_city_description("paris")
        self.assertEqual(description, "Paris")

    def test_get_city_name_and_location(self):
        """ Test if the user input the city name and its location. """
        description = get_city_description("paris", "france")
        self.assertEqual(description, "Paris, France")

unittest.main()
