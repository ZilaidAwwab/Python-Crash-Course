# Write a test case for Employee. Write two test methods, test_give_default_raise() and test_give_custom_raise(). Use the setUp() method so you don’t have to create a new employee instance in each test method. Run your test case, and make sure both tests pass.

import unittest
from employee import Employee


class TestEmployees(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Zilaid", "Awwab", 200000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        assert self.employee.annual_salary == 205000

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        assert self.employee.annual_salary == 210000


unittest.main()
