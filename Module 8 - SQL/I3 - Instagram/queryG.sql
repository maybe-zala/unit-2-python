

-- The data stored in the instagram database are: firstName, surname, career, followersMillions and instagramHandle

 -- Edit the SQL query below so that it displays all of the data of those from our top 10 instagram followers database who are a footballer or have less than 150 million followers. In this search remember to just search for 150 you do not need to write out the number in full. 
SELECT * FROM instagram WHERE followersMillions < 150 OR career = "Footballer";
 -- Remember to refer to the CheatSheet.jpg to help you.

