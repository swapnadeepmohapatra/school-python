import mysql.connector as mc
connector = mc.connect(host="localhost", user="root",
                       passwd="root", database="database_students")

cursor = connector.cursor()

database_delete_entry_command = '''
DELETE FROM students
WHERE name = "Rohit";
'''

cursor.execute(database_delete_entry_command)
connector.commit()
