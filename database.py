from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(1, 10, database="learning", user="postgres", password="1234", host="localhost")
# connection_pool = pool.SimpleConnectionPool(1, 1, database="learning", user="postgres", password="1234", host="localhost")

class CursorFromConnectionPool:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = connection_pool.getconn()
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.cursor.close()
        self.conn.commit()
        connection_pool.putconn(self.conn)
