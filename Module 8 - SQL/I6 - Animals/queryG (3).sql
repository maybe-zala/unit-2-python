-- The data stored in the animals database are: animalName, averageLifeSpanYears, speedMPH, distanceFromSun and conservationStatus

 -- Edit the SQL query below so that it displays the animal names, conservation status and speed of the animals that have the letter O anywhere in their name. Then order the results in order by the fastest to the slowest animal.
select animalName, conservationStatus, speedMPH from animals where animalName like '%o%' order by speedMPH desc;
 -- Remember to refer to the CheatSheets to help you.




 