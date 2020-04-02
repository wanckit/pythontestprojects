import sqlite3 as sql

database = sql.connect('test1.db')

database_cursor = database.cursor()

cmd1 = 'CREATE TABLE users(username TEXT,password TEXT)'
cmd2 = 'INSERT INTO users(username,password) VALUES("testuser","testpassword")'
cmd3 = 'SELECT username,password FROM users'
database_cursor.execute(cmd1)
database_cursor.execute(cmd2)
database_cursor.execute(cmd3)

database.commit()

for x in database_cursor:
    print x



