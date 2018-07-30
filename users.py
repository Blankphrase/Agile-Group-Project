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

    def comment(self, comment, username):
        dict_comm = {}
        #comment = input("enter your comment")
        #username = input("enter your username")
        dict_comm["comment"] = comment
        dict_comm["username"] = username
        self.comments.append(dict_comm)
    
    def view_comments(self):
        for comment in self.comments:
            if comment['username'] == username:
                print(comment['comment'])
        
