import mysql.connector as mc
connector = mc.connect(host="localhost", user="root",
                       passwd="root", database="database_students")

cursor = connector.cursor()

database_get_total_fees_command = '''
SELECT class, SUM(fees)
FROM students
GROUP BY class;
'''

cursor.execute(database_get_total_fees_command)
data = cursor.fetchall()

for item in data:
    print("Class", item[0], "have given total", item[1], "fees")
