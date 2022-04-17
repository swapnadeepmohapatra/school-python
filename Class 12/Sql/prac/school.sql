-- -- CREATE DATABASE IF NOT EXISTS school;

-- -- USE school;

-- -- CREATE TABLE students(
-- -- 	id INT PRIMARY KEY,
-- -- 	name VARCHAR(15) NOT NULL,
-- -- 	mark1 INT,
-- -- 	mark2 INT,
-- -- 	mark3 INT,
-- -- 	mark4 INT,
-- -- 	total INT,
-- -- 	result VARCHAR(15)
-- -- );

-- -- UPDATE students
-- -- SET result = "pass"
-- -- where total > 100;

-- -- UPDATE students
-- -- SET result = "fail"
-- -- where total < 100;

-- -- ALTER TABLE students
-- -- ADD COLUMN gender char(1);

-- -- ALTER TABLE students
-- -- MODIFY COLUMN name varchar(100);

-- -- ALTER TABLE students
-- -- ADD COLUMN subject_combo INT;

-- -- CREATE TABLE subjects(
-- -- 	id INT PRIMARY KEY,
-- -- 	sub1 varchar(10),
-- -- 	sub2 varchar(10),
-- -- 	sub3 varchar(10),
-- -- 	sub4 varchar(10)
-- -- );

-- -- INSERT INTO subjects(id, sub1, sub2, sub3, sub4)
-- -- VALUES
-- -- (1, "Math", "Chem", "Phy", "Eng"),
-- -- (2, "Math", "Eng", "Comp", "Bio"),
-- -- (3, "Math", "Ped", "Chem", "Phy");

-- -- SELECT students.name, subjects.sub1, subjects.sub2
-- -- FROM students, subjects
-- -- WHERE students.subject_combo = subjects.id;

-- SELECT EMP_NO, COUNT(*)
-- FROM EMP
-- GROUP BY EMP_NO
-- HAVING salary > 10;

select stu_fname, login_count, count(*) from students group by login_count having count(*) > 1;