rem CS 448 SQLPLUS Project1
rem Huyue Gu

CREATE TABLE Guide
	(GuidId INTEGER, 
	 FirstName CHAR(20), 
	 LastName CHAR(20),
	 Age INTEGER,
	 MaxCapacity INTEGER);

INSERT INTO  Guide (GuidId, FirstName, LastName, Age, Maxcapacity)
VALUES  (1,'Ruby','Elmagarmid',25,5);

INSERT INTO  Guide (GuidId, FirstName, LastName, Age, Maxcapacity)
VALUES  (2,'Walid','Aref',27,13);

INSERT INTO  Guide (GuidId, FirstName, LastName, Age, Maxcapacity)
VALUES  (3,'Christopher','Clifton',18,4);

INSERT INTO  Guide (GuidId, FirstName, LastName, Age, Maxcapacity)
VALUES  (4,'Sunil','Prabhakar',22,7);

INSERT INTO  Guide (GuidId, FirstName, LastName, Age, Maxcapacity)
VALUES  (5,'Elisa','Bertino', 26,5);

INSERT INTO  Guide (GuidId, FirstName, LastName, Age, Maxcapacity)
VALUES  (6,'Dong','Su',23,3);

INSERT INTO  Guide (GuidId, FirstName, LastName, Age, Maxcapacity)
VALUES  (7,'David','Eberts',24,8);

INSERT INTO  Guide (GuidId, FirstName, LastName, Age, Maxcapacity)
VALUES  (8,'Arif','Ghafoor',20,5);

INSERT INTO  Guide (GuidId, FirstName, LastName, Age, Maxcapacity)
VALUES  (9,'Eduard','Dragut',19,10);

SELECT GuidId FROM Guide;




