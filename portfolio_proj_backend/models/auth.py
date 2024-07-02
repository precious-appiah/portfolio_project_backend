"""this is my auth system to ckeck for both login and sign up"""
import json
import os
from .user import User


class AuthSystem:
    """contains all methods for sign up and login"""

    def __init__(self, filepath='users.json'):
        """initialisation"""
        self.filepath = filepath
        self.users = self.get_users()

    def get_users(self):
        """check if user exist in file"""
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as file:
                json.dump({}, file)
            return {}

        with open(self.filepath, 'r') as file:
            users_dict = {}
            data = json.load(file)
            for email, info in data.items():
                user_obj = User.from_dict(info)
                users_dict[email] = user_obj
            return users_dict

    def save_users(self):
        """this method stores the users in file"""
        with open(self.filepath, 'w') as file:
            json.dump({email: user.to_dict() for email, user in self.users.items()}, file)

    def signup(self, email, username, password, confirmPass):
        """method for signing up"""
        if email in self.users:
            return "Email already taken"
        if password != confirmPass:
            return "Passwords don't match"
        new_user = User(email, username, password)
        self.users[email] = new_user
        self.save_users()
        return "Sign up successful"

    def login(self, email, password):
        """checks for user login """
        for key, info in self.users.items():
            if key == email:
                data = info.__dict__
                if data['password'] == password:
                    return data
                else:
                    return "Incorrect password or email"

        return "Email not registered, please sign up"
