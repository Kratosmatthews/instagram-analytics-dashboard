SELECT gender, AVG(daily_usage_time)
FROM instagram_cleaned
GROUP BY gender;

SELECT age, AVG(engagement)
FROM instagram_cleaned
GROUP BY age;

SELECT occupation, AVG(daily_usage_time)
FROM instagram_cleaned
GROUP BY occupation;