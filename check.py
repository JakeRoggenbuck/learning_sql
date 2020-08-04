import sqlite3
connection = sqlite3.connect("myTable.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM employee")
print("fetchall:")
result = cursor.fetchall()
for r in result:
    print(r)


cursor.execute("SELECT * FROM employee")
result = cursor.fetchall()
for r in result:
    print(f"{r[1]} {r[2]} joined on {r[4]}")


cursor.execute("SELECT * FROM employee")
print("\nfetch one:")
res = cursor.fetchone()
print(res)
