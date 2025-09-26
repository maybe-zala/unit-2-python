-- The data stored in the disney character database are: CharacterName, Film, Gender and CharacterType.

-- 10 Write a query to delete the Queen of Hearts record from the Superheroes and Villain table then display all the records to show that this record has been deleted. 
delete from SuperheroesVillains where CharacterName = 'Queen of Hearts';


select * from SuperheroesVillains;