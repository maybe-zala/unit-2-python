-- The data stored in the disney character database are: CharacterName, Film, Gender and CharacterType.

-- 8 Write a query to show all the records from the Superheroes and Villain table that the letter I in their name.
select * from SuperheroesVillains where CharacterName like '%I%'
 