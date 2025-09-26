-- The data stored in the disney character database are: CharacterName, Film, Gender and CharacterType.

-- 2: Write a query to show all the names of female superhereos from the Superheroes and Villain table.
select CharacterName from SuperheroesVillains where Gender = 'Female' and CharacterType = 'Superhero';

