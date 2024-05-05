# Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 166) or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.


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


class Admin(User):
    def __init__(self, first_name, last_name, age, education, department):
        super().__init__(first_name, last_name, age, education, department)
        self.privileges = ["can add user", "can delete user", "can add post"]

    def show_privileges(self):
        print("The privileges of the admin are:")
        for privilege in self.privileges:
            print(f"\t{privilege}")


admin = Admin("Hussain", "Shah", "32", "MBA", "marketing")
admin.show_privileges()
