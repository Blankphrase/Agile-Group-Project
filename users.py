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

    