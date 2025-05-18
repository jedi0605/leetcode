-- # Write your MySQL query statement below
-- SELECT Students.student_id,Students.student_name,Subjects.subject_name,COUNT( Examinations.subject_name)  as attended_exams
-- -- SELECT *
-- FROM Students
-- JOIN Subjects
-- LEFT JOIN Examinations ON Examinations.student_id = Students.student_id AND Subjects.subject_name = Examinations.subject_name
-- GROUP BY Subjects.subject_name, Students.student_id
-- ORDER BY Students.student_id,Subjects.subject_name


-- SELECT student_id, subject_name, COUNT(subject_name) as cnt
-- FROM Examinations
-- GROUP BY subject_name, student_id

SELECT s.student_id,s.student_name, sub.subject_name,IFNULL(grouped.attended_exams, 0) AS attended_exams
FROM Students AS s
JOIN Subjects AS sub
LEFT JOIN (
    SELECT student_id, subject_name, COUNT(subject_name) as attended_exams
    FROM Examinations
    GROUP BY subject_name, student_id
) grouped
ON s.student_id = grouped.student_id AND sub.subject_name = grouped.subject_name
ORDER BY s.student_id, sub.subject_name