import mysql.connector
cnx = mysql.connector.connect(user='root',
                              password='admin',
                              host='localhost',
                              database='student')
print(cnx)
cursor = cnx.cursor()
#show all databases
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db[0])
cnx.close()