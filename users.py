import datetime

class Project(object):
    def __init__(self):
        self.user_details = {}
        # stores credentials
        self.credentials = {}
        # stores logged in users
        self.session = {}
    
