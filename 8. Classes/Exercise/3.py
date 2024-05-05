# Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user.Create several instances representing different users, and call both methods for each user


class User:
    def __init__(self, first_name, last_name, age, education, department):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.education = education
        self.department = department

    def describe_user(self):
        print(
            f"This is {self.first_name.title()} {self.last_name.title()}. He is {str(self.age)}, and his education is {self.education}. He is hired in the {self.department} department."
        )

    def greet_user(self):
        full_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"Hello, {full_name}. We are exited to have you on board.")


ahmad = User("ahmad", "rana", 23, "MPhill", "Machine Learning")
ahmad.greet_user()
ahmad.describe_user()

shaheer = User("shaheer", "khan", 21, "PhD", "Data Science")
shaheer.greet_user()
shaheer.describe_user()
