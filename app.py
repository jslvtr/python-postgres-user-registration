from user import User
from database import Database

Database.initialise(database="learning", user="postgres", password="1234", host="localhost")

user = User('jose@schoolofcode.me', 'Jose', 'Salvatierra')

user.save_to_db()

user_from_db = User.load_from_db_by_email('jose@schoolofcode.me')

print(user_from_db)
