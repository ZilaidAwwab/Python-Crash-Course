from survey import AnonymousSurvey

# Define a question to make a survey
question = "What language did you learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question and store the response
my_survey.show_question()
print("Enter 'q' to quit the survey:")
while True:
    response = input("Language: ")
    if response == "q":
        break
    my_survey.store_response(response)

# Show the result
print("Thankyou everyone who participated in the survey.")
my_survey.show_results()
