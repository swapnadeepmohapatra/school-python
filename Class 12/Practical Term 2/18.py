import mysql.connector as mc
connector = mc.connect(host="localhost", user="root",
                       passwd="root", database="database_students")

cursor = connector.cursor()

database_update_fees_command = '''
UPDATE students
SET fees = 20000
WHERE name = "Rohit";
'''

cursor.execute(database_update_fees_command)
connector.commit()
