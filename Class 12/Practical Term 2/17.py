import mysql.connector as mc
connector = mc.connect(host="localhost", user="root",
                       passwd="root", database="database_students")

cursor = connector.cursor()

database_add_new_column_command = '''
ALTER TABLE students
ADD (percentage_in_10_boards INT);
'''

database_change_column_command = '''
ALTER TABLE students
MODIFY percentage_in_10_boards varchar(20);
'''

database_remove_column_command = '''
ALTER TABLE students
DROP COLUMN percentage_in_10_boards;
'''

connector.commit()
