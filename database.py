from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(1, 10, database="learning", user="postgres", password="1234", host="localhost")

# What happens if we do this instead?
# connection_pool = pool.SimpleConnectionPool(1, 1, database="learning", user="postgres", password="1234", host="localhost")
