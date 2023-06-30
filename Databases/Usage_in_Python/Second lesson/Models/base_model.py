import psycopg2

class BaseModel():

    def cone_db():
        conn = psycopg2.connect(
            database='pusage',
            user='postgres',
            password='julia123',
            host='127.0.0.1',
            port='5432'
        )
        return conn