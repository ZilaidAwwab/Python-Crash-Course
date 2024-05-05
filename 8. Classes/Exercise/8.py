# Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.


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


class Privileges:
    def __init__(self):
        self.privileges = ["can add user", "can delete user", "can add post"]

    def show_privileges(self):
        print("The privileges of the admin are:")
        for privilege in self.privileges:
            print(f"\t{privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age, education, department):
        super().__init__(first_name, last_name, age, education, department)
        self.privileges = Privileges()


admin = Admin("Hussain", "Shah", "32", "MBA", "marketing")
admin.privileges.show_privileges()
