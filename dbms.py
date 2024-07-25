import sqlite3

#define connection and cursor

connection = sqlite3.connect('my_databse.db')
cursor = connection.cursor()

# create a people table

command1 = """CREATE TABLE IF NOT EXISTS
people(person_id INTEGER PRIMARY KEY,name TEXT,last_name TEXT)"""

cursor.execute(command1)

#create schools table

command2 = """CREATE TABLE IF NOT EXISTS
schools(school_id INTEGER PRIMARY KEY,name TEXT, person_id INTEGER,FOREIGN KEY(person_id) REFERENCES people(person_id))"""

cursor.execute(command2)


#Add persons
cursor.execute("INSERT INTO people VALUES(1,'Ahmet Emre','Cakir')")

#Add schools
cursor.execute("INSERT INTO schools VALUES(100,0)")


# Make the data persistant ( not permanent) 
connection.commit()

cursor.execute("SELECT * FROM people")
results = cursor.fetchall()
print(results)