import sqlite3
connection = sqlite3.connect("myTable.db")
crsr = connection.cursor()

sql_command = """
CREATE TABLE employee (
staff_number INTEGER PRIMARY KEY,
fname VARCHAR(20),
lname VARCHAR(30),
gender CHAR(1),
joining DATE);"""

crsr.execute(sql_command)
connection.commit()
connection.close()
