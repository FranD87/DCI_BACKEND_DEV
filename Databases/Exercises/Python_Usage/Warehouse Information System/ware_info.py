import psycopg2

conn = psycopg2.connect(
    database='warehouse_information_system',
    user='postgres',
    password='Fran1361987',
    host='127.0.0.1',
    port='5432'
)

cursor = conn.cursor()
cursor.execute('SELECT version();')
db_version = cursor.fetchone()
cursor.execute('SELECT * FROM Employee;')
data = cursor.fetchall()
print(data)



