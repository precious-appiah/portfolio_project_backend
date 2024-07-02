class User:
    """this class defindes a user """
    def __init__(self, email, username, password):
        """initialisation"""
        self.email = email
        self.username = username
        self.password = password

    def to_dict(self):
        """save obj to dict"""
        return self.__dict__

    @staticmethod
    def from_dict(data):
        """static method to """
        return User(**data)
