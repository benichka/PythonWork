class Employee():
    def __init__(self, first, last, annual_salary):
        """ Initialise an employee with his name and its salary. """
        self.first = first
        self.last = last
        self.annual_salary = annual_salary

    def give_raise(self, salary_raise=5000):
        """ Give a raise to an employee. """
        self.annual_salary += salary_raise

