class User:
    def __init__(self, email, first_name, last_name, id=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return "<User {}>".format(self.email)

    def save_to_db(self):
        with psycopg2.connect(database="learning", user="postgres", password="1234", host="localhost") as conn:
            with conn.cursor() as cursor:
                cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)',
                                (self.email, self.first_name, self.last_name))
