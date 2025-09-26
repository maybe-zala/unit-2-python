-- The data stored in the disney character database are: CharacterName, Film, Gender and CharacterType.

-- 3: Write a query to show all the names and type of characters from the Superheroes and Villain table who are in the films X-Men or Guardians of the Galaxy.
select CharacterName, CharacterType from SuperheroesVillains where Film = 'X-Men' or Film = 'Guardians of the Galaxy'

