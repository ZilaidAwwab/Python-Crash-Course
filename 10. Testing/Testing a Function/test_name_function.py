# To write a test case for a function, import the unittest module and the function you want to test. Then create a class that inherits from unittest.TestCase, and write a series of methods to test different aspects of your function’s behavior.

import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    # remember to start the test name from test keyword
    def test_first_last_name(self):
        formatted_name = get_formatted_name("janis", "jopkins")
        self.assertEqual(formatted_name, "Janis Jopkins")

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name("wolfgang", "mozart", "amadeus")
        self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart")


unittest.main()

# Any method that starts with test_ (as we can see that here the method we wrote starts with the name test i-e: test_first_last) will be run automatically when we run test_name_function.py file. Within this test method, we call the function we want to test and store a return value that we’re interested in testing. In this example we call get_formatted_name() with the arguments 'janis' and 'jopkins', and store the result in formatted_name

# At last we use one of unittest’s most useful features: an assert method. Assert methods verify that a result you received matches the result you expected to receive. In this case, because we know get_formatted_name() is supposed to return a capitalized, properly spaced full name, we expect the value in formatted_name to be Janis Joplin. To check if this is true, we use unittest’s assertEqual() method and pass it formatted_name and 'Janis Jopkins'.

# The line unittest.main() tells Python to run the tests in this file
