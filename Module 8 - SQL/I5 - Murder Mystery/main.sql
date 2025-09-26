.open sql-murder-mystery.db
.mode column

-- Write one query at a time starting on line 8 below. We have started the first one for you.

-- Comment out your query once you have taken a note of your answer using your detective notes and then start your next query. 

INSERT INTO solution VALUES (1, 'Miranda Priestly');
SELECT value FROM solution

--SELECT date, type, description, city FROM crime_scene_report WHERE date = 20180115 AND city = "SQL City" AND type = "murder"

--SELECT person_id,transcript FROM interview

--SELECT license_id,id, name FROM person WHERE address_street_name = "Franklin Ave"

--SELECT license_id,id, name, address_number FROM person WHERE address_street_name = "Northwestern Dr" ORDER BY address_number DESC;

--SELECT id, person_id, name FROM get_fit_now_member WHERE id = "16371"

--SELECT * FROM interview WHERE person_id = 14887
--I heard a gunshot and then saw a man run out. He had a "Get Fit Now Gym" bag. The membership number on the bag started with "48Z". Only gold members have those bags. The man got into a car with a plate that included "H42W".

SELECT id, person_id, name FROM get_fit_now_member WHERE id LIKE '48Z%'

SELECT * FROM person WHERE name = "Jeremy Bowers"

SELECT * FROM drivers_license WHERE id = "423327"

--BREAK-------------------------------------------------------------------

SELECT * FROM interview WHERE person_id = 67318	
--I was hired by a woman with a lot of money. I don't know her name but I know she's around 5'5" (65") or 5'7" (67"). She has red hair and she drives a Tesla Model S. I know that she attended the SQL Symphony Concert 3 times in December 2017.
SELECT * FROM drivers_license WHERE gender = "female" AND car_make = "Tesla" AND car_model = "Model S"

SELECT * FROM person WHERE license_id = 202298