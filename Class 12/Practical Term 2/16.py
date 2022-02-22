import mysql.connector as mc
connector = mc.connect(host="localhost", user="root",
                       passwd="root", database="database_students")

cursor = connector.cursor()

database_create_command = '''
CREATE TABLE students (
    roll INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    class INT,
    course ENUM('Sc','Com','Hum'),
    fees INT,
    age INT
);
'''

cursor.execute(database_create_command)


def insert_into_database_values(values):
    insert_command = "INSERT INTO students (name, class, course, fees, age) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(insert_command, values)


insert_into_database_values(("Rohit", 12, "Sc", 10000, 18))
insert_into_database_values(("Mohit", 11, "Sc", 20000, 16))
insert_into_database_values(("Purohit", 12, "Hum", 15000, 18))
insert_into_database_values(("Lohit", 11, "Hum", 25000, 17))
insert_into_database_values(("Udit", 12, "Com", 17000, 17))

connector.commit()
