WITH TeacherGradingCounts AS (
    SELECT teacher_id, COUNT(*) AS total_graded
    FROM assignments
    WHERE state = 'GRADED'
    GROUP BY teacher_id
    ORDER BY total_graded DESC
    LIMIT 1
)
SELECT COUNT(*) 
FROM assignments 
WHERE state = 'GRADED' 
AND grade = 'A' 
AND teacher_id = (SELECT teacher_id FROM TeacherGradingCounts);