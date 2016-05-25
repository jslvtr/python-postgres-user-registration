class User:
    def __init__(self, email, first_name, last_name, id=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return "<User {}>".format(self.email)
