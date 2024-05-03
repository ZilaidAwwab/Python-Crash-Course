# Letting the user choose when to quit

prompt = "Tell me something and I will repeat it after you"
prompt += "\nEnter quit to end the program: "

message = ""

while message != "quit":
    message = input(prompt)

    if message != "quit":
        print(message)
