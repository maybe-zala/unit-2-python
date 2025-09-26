-- The data stored in the animals database are: animalName, averageLifeSpanYears, speedMPH, distanceFromSun and conservationStatus

 -- Edit the SQL query below so that it displays the animal names, average life span and speed of the animals that have the letter E anywhere in their name. Then order the results in descending order by animal name.
select animalName, averageLifeSpanYears, speedMPH from animals where animalName like '%e%' order by animalName desc;
 -- Remember to refer to the CheatSheets to help you.




 