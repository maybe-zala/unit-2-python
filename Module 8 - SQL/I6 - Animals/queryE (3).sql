-- The data stored in the animals database are: animalName, averageLifeSpanYears, speedMPH, distanceFromSun and conservationStatus

 -- Edit the SQL query below so that it displays all of the animal names of those whose conservation status are endangered and order results in ascending order by animal name.
select animalName from animals where conservationStatus = 'Endangered' order by animalName;
 -- Remember to refer to the CheatSheets to help you.



 