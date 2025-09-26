

-- The data stored in the planets database are: planetName, numMoons, firstYearRecorded, distanceFromSun and discoveredBy

 -- Create a SQL query below so that it displays only the planet name and year discovered of the planets that were NOT discovered by Galileo Galilei. Display the results in descending order by year discovered.
 SELECT planetName,firstYearRecorded FROM planets WHERE discoveredBy != 'Galileo Galilei' ORDER BY firstYearRecorded DESC;
 -- Remember to refer to the CheatSheet.jpg to help you. You will need knowledge from bronze level to help complete this task. Refer to the BronzeCheatSheet.jpg to help refresh your memory on WHERE commands if needed.



 