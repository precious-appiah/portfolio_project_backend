"""this is my auth system to ckeck for both login and sign up"""
import json
import os
from .user import User
from .task import Task


class AuthSystem:
    """contains all methods for sign up and login"""

    def __init__(self):
        """initialisation"""
        self.user_filepath = 'users.json'
        self.task_filepath = 'tasks.json'
        self.users = self.get_users()
        self.tasks = self.load_tasks()

    def get_users(self):
        """check if user exist in file"""
        if not os.path.exists(self.user_filepath):
            with open(self.user_filepath, 'w') as file:
                json.dump({}, file)
            return {}
    
        with open(self.user_filepath, 'r') as file:
            users_dict = {}
            data = json.load(file)
            for email, info in data.items():
                user_obj = User.from_dict(info)
                users_dict[email] = user_obj
            return users_dict

    def load_tasks(self):
        """get saved tasks"""
        if not os.path.exists(self.task_filepath):
            with open(self.task_filepath, 'w') as file:
                json.dump({}, file)
            return {}
        
        with open(self.task_filepath, 'r') as file:
            data = json.load(file)
        return {email: [Task(task['task'], task['id'], task['is_completed']) for task in tasks] for email, tasks in data.items()}


    def save_users(self):
        """this method stores the users in file"""
        with open(self.user_filepath, 'w') as file:
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
    
    def save_tasks(self):
        """save tasks in file"""
        with open(self.task_filepath, 'w') as file:
            json.dump({email: [task.to_dict() for task in tasks] for email, tasks in self.tasks.items()}, file)

    def add_task(self, email, task, id, status):
        """add task"""
        task = Task(task, id, status)
        if email not in self.tasks:
            self.tasks[email] = []
        self.tasks[email].append(task)
        self.save_tasks()
        return "Task added successfully."
    
    def get_tasks(self, email):
        """get saved tasks by user"""
        return [task.to_dict() for task in self.tasks.get(email, [])]

    def remove_task(self, email, task_id):
        """delete task using id"""
        self.tasks[email] = [task for task in self.tasks[email] if task.id != task_id]
        self.save_tasks()
        return "Task removed successfully."
    
    def update_task(self, email, task_id, title=None, is_completed=None):
        """update existing tasks"""
        for task in self.tasks[email]:
            if task.id == task_id:
                if title is not None:
                    task.task = title
                if is_completed is not None:
                    task.is_completed = is_completed
                self.save_tasks()
                return "Task updated successfully."
        return "Task not found."
