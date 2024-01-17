-- ranks country origins of bands, ordered by the number of (non-unique) fans
-- basic select statement to get specific columns
SELECT origin, SUM(fans) AS nb_fans FROM holberton.metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
