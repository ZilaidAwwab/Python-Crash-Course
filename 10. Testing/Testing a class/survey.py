class AnonymousSurvey:
    """Collect anonymous answers to random questions"""

    def __init__(self, question):
        """Store a question and prepare to store response"""
        self.question = question
        self.response = []

    def show_question(self):
        """Display the survey question"""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to a survey"""
        self.response.append(new_response)

    def show_results(self):
        """Show all the responses that have been given"""
        print("Survey Answers:")
        for responses in self.response:
            print("- " + responses)


# Implementing such changes would risk affecting the current behavior of the class AnonymousSurvey. For example, it’s possible that while trying to allow each user to enter multiple responses, we could accidentally change how single responses are handled. To ensure we don’t break existing behavior as we develop this module, we can write tests for the class.
