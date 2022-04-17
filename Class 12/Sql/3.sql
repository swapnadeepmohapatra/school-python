-- Conact
SELECT CONCAT(stu_fname, " ", stu_lname) AS FullName from students;
 
CONCAT(stu_fname, ' ', stu_lname, ' and login count is ',  login_count) 
AS 'full Info' 
from students;

-- Replace
SELECT REPLACE (email, '@', '_') from students;

-- Substring
SELECT SUBSTRING(email, 1, 7) AS TRUNCATED from students;

SELECT CONCAT(SUBSTRING(email, 1, 7), "...") AS TRUNCATED from students;

-- Reverse
SELECT REVERSE(email) AS reversed_mail from students;

-- Char Length
SELECT email, CHAR_LENGTH(email) AS length from students;

-- Upper Case and Lower Case
SELECT UPPER(stu_fname) AS upper_first_name, LOWER(stu_lname) AS lower_last_name from students;