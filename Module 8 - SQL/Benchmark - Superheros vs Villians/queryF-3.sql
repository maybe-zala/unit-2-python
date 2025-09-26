-- The data stored in the disney character database are: CharacterName, Film, Gender and CharacterType.

-- 6 Write a query to show all the records from the Superheroes and Villain table that have a name starting with the letter M.
select * from SuperheroesVillains where CharacterName like 'M%';

