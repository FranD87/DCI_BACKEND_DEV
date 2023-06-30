import sqlite3


class Database:
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            cls.__instance.connction = sqlite3.connect('example.db')
        return cls.__instance

    def execute(self, query):
        cursor = self.connction.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        return result

db1 = Database()

print(db1)

result = db1.execute("select * from users")
print(result)

