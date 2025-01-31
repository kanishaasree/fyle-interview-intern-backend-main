SELECT grade, COUNT(*) as count
FROM assignments
WHERE state = 'GRADED'
GROUP BY grade
ORDER BY grade;