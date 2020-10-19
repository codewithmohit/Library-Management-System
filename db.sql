CREATE DATABASE  IF NOT EXISTS `library` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `library`;
-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `authors`
--

DROP TABLE IF EXISTS `authors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authors` (
  `idauthors` int NOT NULL AUTO_INCREMENT,
  `author_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idauthors`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authors`
--

LOCK TABLES `authors` WRITE;
/*!40000 ALTER TABLE `authors` DISABLE KEYS */;
INSERT INTO `authors` VALUES (1,'Harivansh Ray Bachchan'),(2,'K D Pathak'),(3,'mannu '),(6,'taarak'),(7,'Robert Macmallin');
/*!40000 ALTER TABLE `authors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `idbook` int NOT NULL AUTO_INCREMENT,
  `book_name` varchar(45) DEFAULT NULL,
  `book_category` varchar(30) DEFAULT NULL,
  `book_code` varchar(45) DEFAULT NULL,
  `book_description` varchar(100) DEFAULT NULL,
  `book_author` varchar(30) DEFAULT NULL,
  `book_publisher` varchar(30) DEFAULT NULL,
  `book_price` int DEFAULT NULL,
  `total_books` int DEFAULT NULL,
  PRIMARY KEY (`idbook`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (9,'Avengers','Marvel','552','Very Interesting.','K D Pathak',' comic',5000,38),(10,'abc','Avengers','522','Nice Book','Harivansh Ray Bachchan','Marvel',522,34),(11,'Singularity is Near','Sci-fi','vh26869gdg','The book is abot the simulation of the AI technology','Robert Macmallin','MIT Publication',6000,5);
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `idcategory` int NOT NULL AUTO_INCREMENT,
  `category_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idcategory`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'Avengers'),(2,'Marvel'),(3,'abc'),(4,'xyz'),(5,'jhkjh'),(7,'action'),(9,'dsfsd'),(10,'laptop'),(11,'Sci-fi');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dayoperation`
--

DROP TABLE IF EXISTS `dayoperation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dayoperation` (
  `iddayoperation` int NOT NULL AUTO_INCREMENT,
  `book_name` varchar(45) DEFAULT NULL,
  `roll_no` varchar(45) DEFAULT NULL,
  `type` varchar(30) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `to_date` datetime DEFAULT NULL,
  PRIMARY KEY (`iddayoperation`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dayoperation`
--

LOCK TABLES `dayoperation` WRITE;
/*!40000 ALTER TABLE `dayoperation` DISABLE KEYS */;
INSERT INTO `dayoperation` VALUES (24,'abc','17EIACS045','Retrieve','2020-06-26 00:00:00','2020-06-27 00:00:00'),(26,'abc','17EIACS045','Rent','2020-06-26 00:00:00','2020-06-30 00:00:00'),(27,'abc','17EIACS045','Rent','2020-06-26 00:00:00','2020-06-30 00:00:00'),(28,'abc','17EIACS045','Rent','2020-06-26 00:00:00','2020-06-30 00:00:00'),(29,'abc','17EIACS045','Retrieve','2020-06-26 00:00:00','2020-06-27 00:00:00'),(30,'abc','17EIACS045','Retrieve','2020-06-26 00:00:00','2020-06-27 00:00:00'),(31,'abc','12345678','Rent','2020-06-27 00:00:00','2020-06-28 00:00:00');
/*!40000 ALTER TABLE `dayoperation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `publisher`
--

DROP TABLE IF EXISTS `publisher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `publisher` (
  `idpublisher` int NOT NULL AUTO_INCREMENT,
  `publisher_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idpublisher`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `publisher`
--

LOCK TABLES `publisher` WRITE;
/*!40000 ALTER TABLE `publisher` DISABLE KEYS */;
INSERT INTO `publisher` VALUES (1,'Marvel'),(2,'Studio'),(3,'dc'),(4,' comic'),(5,'mehta'),(6,'MIT Publication');
/*!40000 ALTER TABLE `publisher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `idstudent` int NOT NULL AUTO_INCREMENT,
  `roll_no` varchar(45) DEFAULT NULL,
  `student_name` varchar(45) DEFAULT NULL,
  `branch` varchar(45) DEFAULT NULL,
  `mobile_no` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idstudent`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (5,'17EIACS045','Abc','C.S.E.','9523647812','abc@gmail.com'),(6,'12345678','James','CSE','6548975645','lib45658@iet.com');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `idUSERS` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(45) DEFAULT NULL,
  `user_email` varchar(45) DEFAULT NULL,
  `user_password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idUSERS`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'abc','abc@gmail.com','12345'),(2,'qwerty','vineetfeb14@gmail.com','qwerty'),(3,'asdf','sdfgh','qwe');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-29 16:34:22
