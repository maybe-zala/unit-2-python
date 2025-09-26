-- The data stored in the disney character database are: CharacterName, Film, Gender and CharacterType.

-- 5 Write a query to show all the types of character then the names from the Superheroes and Villain table in alphabetical order (A to Z) by character type then descending order by character name.

select CharacterType, CharacterName from SuperheroesVillains order by CharacterType, CharacterName desc
