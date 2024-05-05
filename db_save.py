import mysql.connector

cnx = mysql.connector.connect(user='root',
                              password='admin',
                              host='localhost',
                              database='student')

cnx.close()