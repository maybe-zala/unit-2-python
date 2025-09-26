

-- The data stored in the instagram database are: firstName, surname, career, followersMillions and instagramHandle

 -- Edit the SQL query below so that it displays on the first name, surname and instagram handle of those from our top 10 instagram followers database who have less than or equal to 155 million followers. In this search remember to just search for 155 you do not need to write out the number in full. 
SELECT firstName, surname, instagramHandle FROM instagram WHERE followersMillions <= 155;
 -- Remember to refer to the CheatSheet.jpg to help you.

