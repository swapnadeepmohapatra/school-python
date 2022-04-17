-- Unique Email Address
SELECT DISTINCT email FROM students;

-- Order by
SELECT DISTINCT stu_fname, login_count, course_count 
FROM students
ORDER BY login_count ASC;

SELECT DISTINCT stu_fname, login_count, course_count 
FROM students
ORDER BY course_count DESC;

-- Limit
SELECT DISTINCT stu_fname
FROM students
LIMIT 5;

SELECT DISTINCT stu_fname
FROM students
LIMIT 2, 5;

-- Like: Pattern Matching
SELECT stu_fname
FROM students
WHERE stu_fname
LIKE "%esh";

-- Count
SELECT COUNT(*)
FROM students;

SELECT COUNT(DISTINCT stu_fname)
FROM students;

-- SQL Mode
SET @@sql_mode='';

-- Group by
SELECT stu_fname, signup_month, COUNT(*) from students
GROUP BY signup_month;

-- Min and Max
SELECT MIN(login_count) from students;

SELECT stu_fname, email, login_count from students
WHERE login_count = (SELECT MAX(login_count) from students);

-- Group by with Min, Max
SELECT MAX(login_count), signup_month from students
GROUP BY signup_month ORDER BY signup_month;

-- Sum and Avg
SELECT signup_month, AVG(login_count) from students
GROUP BY signup_month;

SELECT signup_month, SUM(login_count) from students
GROUP BY signup_month
ORDER BY signup_month;

-- And and or
SELECT stu_fname, email, login_count from students
WHERE login_count = 9;

SELECT stu_fname, email, signup_month from students
WHERE signup_month <= 5 AND signup_month >= 3;

-- Range: Between and And
SELECT email, login_count, signup_month from students
WHERE signup_month BETWEEN 3 AND 5;

-- Switch Case
SELECT stu_fname, signup_month,
    CASE
        WHEN signup_month BETWEEN 7 AND 10 THEN 'EARLY BIRD'
        WHEN signup_month BETWEEN 11 AND 12 THEN 'REGULAR USER'
        ELSE '##'
    END AS Custom
from students;