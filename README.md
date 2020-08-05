#learning_sql

## Connecting
```
connection = sqlite3.connect("myTable.db")
```

## Creating a table
```
 sql_command = """
 CREATE TABLE employee (
 staff_number INTEGER PRIMARY KEY,
 fname VARCHAR(20),
 lname VARCHAR(30),
 gender CHAR(1),
 joining DATE);"""
```

## Writing the empty table to the db
```
crsr = connection.cursor()
crsr.execute(sql_command)
connection.commit()
```

## Writing values to db
### Getting data
```
First = input("First: ")
Last = input("Last: ")
Gender = input("Gender: ")
Joining = input("Joining: ")
```
### Adding data to the correct syntax
```
sql_command = "INSERT INTO employee"
sql_fields = "(staff_number, fname, lname, gender, joining)"
sql_data = f"VALUES (NULL, '{First}', '{Last}', '{Gender}', '{Joining}');"
```
### Excecuting the command
```
cursor.execute(sql_command + sql_fields + sql_data)
```
### Make sure to commit and close
```
connection.commit()
connection.close()
```

