from psycopg2 import pool

class ConnectionPool:
    def __init__(self):
        # We create a new connection pool
        self.connection_pool = pool.SimpleConnectionPool(1, 10, database="learning", user="postgres", password="1234", host="localhost")

    def __enter__(self):
        # We get a connection from the connection pool
        return self.connection_pool.getconn()

    def __exit__(self, exception_type, exception_value, exception_traceback):
        # We really should be returning connections here, but how can we?
        pass
