-- The data stored in the disney character database are: CharacterName, Film, Gender and CharacterType.

-- 9 Write a query update the name of the character Groot to Baby Groot in the Superheroes and Villain table then display all details of this record to show it has been updated in the database
update SuperheroesVillains set CharacterName = 'Baby Groot' where CharacterName = 'Groot';


select * from SuperheroesVillains