import psycopg2

def connection():
    return psycopg2.connect(database="learning", user="postgres", password="1234", host="localhost")
