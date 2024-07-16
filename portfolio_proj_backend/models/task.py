"""this module defines how every task"""

class Task:
    """task obj"""

    def __init__(self, task, id, is_completed):
        """initialisation"""
        self.task = task
        self.id = id
        self.is_completed = is_completed

    def to_dict(self):
        """returns a dict representation of task"""
        return self.__dict__
    
    @staticmethod
    def from_dict(data):
        return Task(**data)
