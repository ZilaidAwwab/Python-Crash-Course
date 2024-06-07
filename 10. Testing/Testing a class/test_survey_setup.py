# When you include a setUp()method in a TestCase class, Python runs the setUp() method before running each method starting with test_. Any objects created in the setUp() method are then available in each test method you write

# Let’s use setUp() to create a survey instance and a set of responses that can be used in test_store_single_response() and test_store_three_responses():

import unittest
from survey import AnonymousSurvey


class TestAnonymousFunction(unittest.TestCase):
    """Test for class anonymous survey"""

    # This is the helper function of a sort
    def setUp(self):
        """Create a survey and a set response for all test methods"""

        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["English", "Mandarin", "French"]

    def test_store_single_response(self):
        """Testing if a single response is stored properly"""

        self.my_survey.store_response(self.responses[0])

        self.assertIn(self.responses[0], self.my_survey.response)

    # Adding more test cases
    def test_store_three_response(self):
        """Testing that three responses are stored properly"""

        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.response)


unittest.main()
