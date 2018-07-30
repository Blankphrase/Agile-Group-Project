import datetime


class Project(object):
    def __init__(self):
        self.user_details = []
        # stores logged in users
        self.session = {}
        # stores comments
        self.comment = []

    def register(self, username, password):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        self.user_details.append({
            "username": username,
            "password": password
        })
        print("User successfully created")

    def login(self):
        user_name = input("Please Enter User Name")
        user_pass = input("Please Enter Your Password")

        if user_name in self.user_details:
            if user_pass == self.user_details[user_name]['password']:
                self.session.update(self.user_details)
