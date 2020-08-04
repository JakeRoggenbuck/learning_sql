import sqlite3
connection = sqlite3.connect("myTable.db")

cursor = connection.cursor()

First = input("First: ")
Last = input("Last: ")
Gender = input("Gender: ")
Joining = input("Joining: ")

sql_command = "INSERT INTO employee"
sql_fields = "(staff_number, fname, lname, gender, joining)"
sql_data = f"VALUES (NULL, '{First}', '{Last}', '{Gender}', '{Joining}');"

cursor.execute(sql_command + sql_fields + sql_data)

connection.commit()
connection.close()
