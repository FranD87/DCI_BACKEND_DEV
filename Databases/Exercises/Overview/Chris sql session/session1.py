import sqlite3

database_connection = sqlite3.connect('my_friends_table.sql')

create_table_stmnt = '''
    Create Table just_friends(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    location TEXT,
    email TEXT,
    username TEXT
    
    
    )'''

database_connection.execute(create_table_stmnt)