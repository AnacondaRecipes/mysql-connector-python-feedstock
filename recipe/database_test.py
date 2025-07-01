import mysql.connector
import sys

cnx = mysql.connector.connect(
    user="root",
    password="",
    unix_socket=sys.argv[1]
)
cursor = cnx.cursor()
cursor.execute("SELECT VERSION()")
print("Server vesrion:", cursor.fetchone()[0])

cursor.execute("CREATE DATABASE IF NOT EXISTS test_db")
cursor.execute("USE test_db")
cursor.execute("CREATE TABLE t(id INT PRIMARY KEY, txt VARCHAR(30))")
cursor.execute("INSERT INTO t VALUES(1,'---IT WORKS---')")
cnx.commit()
cursor.execute("SELECT * FROM t")
result = cursor.fetchall()
print(result)
assert(result[0] == (1, '---IT WORKS---'))

cursor.close()
cnx.close()
