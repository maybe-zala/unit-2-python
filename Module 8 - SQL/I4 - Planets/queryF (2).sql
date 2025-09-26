-- The data stored in the planets database are: planetName, numMoons, firstYearRecorded, distanceFromSun and discoveredBy

 -- Create a SQL query below so that it displays all of the data the planets that Galileo Galilei discovered and order by distance from the sun in ascending order.
SELECT * FROM planets WHERE discoveredBy = 'Galileo Galilei' ORDER BY distanceFromSun;
 -- Remember to refer to the CheatSheet.jpg to help you. You will need knowledge from bronze level to help complete this task. Refer to the BronzeCheatSheet.jpg to help refresh your memory on WHERE commands if needed.




 