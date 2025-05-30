import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',
    port = '3306',
    user = 'root',
    password = 'password'
)

cursor = connection.cursor()

cursor.execute('SHOW DATABASES;')
records = cursor.fetchall()
print(records)