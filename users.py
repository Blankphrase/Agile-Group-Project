import datetime

class Project(object):
    def __init__(self):
        self.user_details = {}
        # stores logged in users
        self.session = {}

     def register(self):
     	firstname = input("Enter your firstname: ")
     	lastname = input("Enter your lastname: ")
     	username = input("Enter your username: ")
     	email = input("Enter your email: ")
     	password = input("Enter your password: ")
     	self.user_details.update({
     		user: {
     		"firstname":firstname,
     		"lastname":lastname,
     		"username":username,
     		"email":email,
     		"password":password
     		}
     		})
        print("User successfully created")
