-- DO NOT EDIT 
-- Data showing data of planets not including Earth

CREATE TABLE planets (
   planetName varchar(40), 
   numMoons int,
   firstYearRecorded varchar(10),
   distanceFromSun varchar(40), 
   discoveredBy varchar(30)
);

INSERT INTO planets VALUES ("Mercury", 0, "250BC", "58.835 million km", "Galileo Galilei");

INSERT INTO planets VALUES ("Venus", 0, "1610", "107.57 million km", "Galileo Galilei");

INSERT INTO planets VALUES ("Mars", 2, "1610", "212.98 million km", "Galileo Galilei");

INSERT INTO planets VALUES ("Jupiter", 79, "1610", "766.93 million km", "Galileo Galilei");

INSERT INTO planets VALUES ("Saturn", 62, "1610", "1.4931 billion km", "Galileo Galilei");

INSERT INTO planets VALUES ("Uranus", 27, "1781", "2.9592 billion km", "William Herschel");

INSERT INTO planets VALUES ("Neptune", 14, "1846", "4.4762 billion km", "Urbain Le Verrier");



