-- Edit this code below
CREATE TABLE top_gun_actors(
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    month TEXT NOT NULL,
    age INT NOT NULL
);

INSERT INTO top_gun_actors(first_name, last_name, month, age) VALUES ('Tom','Cruise', 'July', 63);
INSERT INTO top_gun_actors(first_name, last_name, month, age) VALUES ('Glenn','Powell', 'October', 36);
INSERT INTO top_gun_actors(first_name, last_name, month, age) VALUES ('Lewis','Pullman', 'January', 32);
INSERT INTO top_gun_actors(first_name, last_name, month, age) VALUES ('Miles','Teller', 'Febuary', 38);
INSERT INTO top_gun_actors(first_name, last_name, month, age) VALUES ('Monica','Barbaro', 'June', 35);

SELECT * FROM top_gun_actors;

-- 1. Add a CREATE TABLE command.
--    1.1 Give the table a name
--    1.2 We want to store firstname, surname, month born and age.
--    1.3 Set the right data types; varchar - used for text or text and numbers like a car number plate. int - used for numbers.



-- 2.Insert data into your table using the INSERT commands. 
--     If you are storing a varchar it must be in " " but if you are storing a int it doesn't need any " "



-- 3.Display your data and your table.


