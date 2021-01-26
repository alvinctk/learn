Find the most networked senator. That is, the one with the most mutual cosponsorships.
A mutual cosponsorship refers to two senators who have each cosponsored a bill sponsored by the other. Even if a pair of senators have cooperated on many bills, the relationship still counts as one.
```sql

WITH mutuals AS (
	SELECT DISTINCT
  		a.sponsor_name AS senator1,
  		a.sponsor_state AS state,
  		b.sponsor_name AS senator2
  	FROM
  		cosponsors a
  	JOIN cosponsors b
  		ON a.sponsor_name = b.cosponsor_name 
  		AND a.cosponsor_name = b.sponsor_name
), mutual_counts AS (
	SELECT
  		senator1 AS senator,
		state,
  		COUNT(*) AS mutual_count
	FROM
		mutuals
	GROUP BY
		senator,
		state
	ORDER BY
		mutual_count
), 
max_mutual_counts AS (
	SELECT
  		state,
  		MAX(mutual_count) AS max_mutual_count
  	FROM
  		mutual_counts
  	GROUP BY
  		state
)

SELECT
	c.state,
	c.senator,
	c.mutual_count
FROM
	mutual_counts c
JOIN
	max_mutual_counts m
	ON c.state = m.state
	AND c.mutual_count = m.max_mutual_count

```

 Find the senators who cosponsored but didn't sponsor bills.

 ```sql
SELECT DISTINCT
	a.cosponsor_name
FROM
	cosponsors a
LEFT JOIN 
	cosponsors b 
	ON a.cosponsor_name = b.sponsor_name
WHERE
	b.sponsor_name IS NULL 
 ```
Using `LEFT JOIN` + `NULL` is a standard trick for excluding rows in table `b`.
