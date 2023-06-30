import psycopg2

conn = psycopg2.connect(
    database='pusage', 
    user='postgres', 
    password='julia123', 
    host='127.0.0.1',
    port='5432'
    )
cursor = conn.cursor()
cursor.execute('SELECT version();')
db_version = cursor.fetchone()
print(db_version)
cursor.execute('CREATE TABLE IF NOT EXISTS test1 (id SERIAL PRIMARY KEY, num INT, data VARCHAR(255));')
cursor.execute("INSERT INTO test1 (num, data) VALUES (12, 'test_val'), (87, 'Test_val 2'), (98, 'Test_val 3');")
cursor.execute('SELECT * FROM test1;')
data = cursor.fetchone()
data_all = cursor.fetchall()
data_2 = cursor.fetchmany(2)
cursor.execute("INSERT INTO test1 (num, data) VALUES (%s, %s)", ('BLA-BLA', 22))
cursor.execute("INSERT INTO test1 (num, data) VALUES (%(number)s, %(my_data)s)", {'my_data': 'test data 100', 'number': 55})
my_number = input('Enter number')
my_data = input('Enter some data')
cursor.execute("INSERT INTO test1 (num, data) VALUES (%(number)s, %(my_data)s)", {'number': my_number, 'my_data': my_data})
cursor.execute("INSERT INTO test1 (num, data) VALUES (" + my_number + ", '" + my_data + "');" )
cursor.execute('SELECT * FROM test1;')
data = cursor.fetchall()
conn.commit()

print(data)


cursor_julia = conn.cursor()

try:
   cursor_julia.execute('SELECT * FROM bla;')
   conn.commit()
except (Exception, psycopg2.Error) as error:
   conn.commit()
   print(f'HERE is error{error}')
conn.close()


