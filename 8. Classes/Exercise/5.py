# Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166). Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0.

# Make an instance of the User class and call increment_login_attempts()several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.


class User:
    def __init__(self, first_name, last_name, age, education, department):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.education = education
        self.department = department

        self.login_attempts = 0

    def describe_user(self):
        print(
            f"This is {self.first_name.title()} {self.last_name.title()}. He is {str(self.age)}, and his education is {self.education}. He is hired in the {self.department} department."
        )

    def reset_login_attempts(self):
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def greet_user(self):
        full_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"Hello, {full_name}. We are exited to have you on board.")


ahmad = User("ahmad", "rana", 23, "MPhill", "Machine Learning")
ahmad.greet_user()
ahmad.describe_user()

shaheer = User("shaheer", "khan", 21, "PhD", "Data Science")
shaheer.greet_user()
shaheer.describe_user()

print(ahmad.login_attempts)
ahmad.increment_login_attempts()

ahmad.reset_login_attempts()
print(ahmad.login_attempts)
