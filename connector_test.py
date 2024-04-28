import mysql.connector

connection = mysql.connector.connect (
    user = 'root' ,
    database = 'elite102' ,
    password = 'hhhggg123' ,
)

cursor = connection.cursor()
testQuery = ("SELECT * FROM user_accounts")
testQuery = ("SELECT * FROM transactions")
cursor.execute(testQuery)

for item in cursor:
    print(item)

connection.commit()

cursor.close()
connection.close()
