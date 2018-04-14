import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """ Test for the class Employee. """
    
    def setUp(self):
        """ Initialise class variable. """
        self.my_employee = Employee("Benoit", "Masson-Bedeau", 36000)

    def test_give_default_raise(self):
        """ Test the default raise for an employee. """
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 41000)

    def test_give_custom_raise(self):
        """ Test a custom raise for an employee. """
        self.my_employee.give_raise(1000)
        self.assertEqual(self.my_employee.annual_salary, 37000)

unittest.main()
