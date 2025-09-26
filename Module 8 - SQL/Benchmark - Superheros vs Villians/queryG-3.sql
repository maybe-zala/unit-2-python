-- The data stored in the disney character database are: CharacterName, Film, Gender and CharacterType.

-- 7 Write a query to show the name, film and type of character of all the villains from the Superhero and Villains table that have a name ending with the letter N.
select CharacterName, Film, CharacterType from SuperheroesVillains where CharacterName like "%n";

