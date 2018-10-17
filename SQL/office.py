from sqlite3 import connect
connection = connect('company.db')
cursor = connection.cursor()
cursor.execute('PRAGMA foreign_keys = 1')


#ESCRIBIR LOS COMANDO SIEMPRE EN MAYUSCULA
sql_command = """
    CREATE TABLE IF NOT EXISTS office(
        id INTEGER PRIMARY KEY,
        name VARCHAR(20) 
    );
    """
 
    
cursor.execute(sql_command)
new_office = input('New office')
sql_command = f'INSERT INTO office(id, name) VALUES (NULL, "{new_office}")'
cursor.execute(sql_command)

sql_command = 'SELECT * FROM office'
cursor.execute(sql_command)

result = cursor.fetchall()
column_names = list(map(lambda x:x[0], cursor.description))
print(column_names)
print(result)

connection.commit()
connection.close()