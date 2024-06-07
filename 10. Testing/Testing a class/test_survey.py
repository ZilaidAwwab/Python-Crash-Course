import unittest
from survey import AnonymousSurvey


class TestAnonymousFunction(unittest.TestCase):
    """Test for class anonymous survey"""

    def test_store_single_response(self):
        """Testing if a single response is stored properly"""

        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("English")

        self.assertIn("English", my_survey.response)

    # Adding more test cases
    def test_store_three_response(self):
        """Testing that three responses are stored properly"""

        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ["English", "Mandarin", "French"]
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.response)


unittest.main()


# This works perfectly. However, these tests are a bit repetitive, so we’ll use another feature of unittest to make them more efficient.
