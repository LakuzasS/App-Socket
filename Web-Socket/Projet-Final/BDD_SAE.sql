-- MySQL dump 10.13  Distrib 8.0.35, for Win64 (x86_64)
--
-- Host: localhost    Database: test
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `clients`
--

DROP TABLE IF EXISTS `clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clients` (
  `client_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `alias` varchar(255) NOT NULL,
  `password_hash` varchar(64) NOT NULL,
  `status` varchar(20) DEFAULT 'disconnected',
  PRIMARY KEY (`client_id`),
  KEY `idx_username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clients`
--

LOCK TABLES `clients` WRITE;
/*!40000 ALTER TABLE `clients` DISABLE KEYS */;
INSERT INTO `clients` VALUES (1,'admin','admin','8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918','disconnected'),(2,'toto','toto','31f7a65e315586ac198bd798b6629ce4903d0899476d5741a9f32e2e521b6a66','disconnected'),(3,'server','server','b3eacd33433b31b5252351032c9b3e7a2e7aa7738d5decdf0dd6c62680853c06','disconnected'),(5,'titi','titi','cce66316b4c1c59df94a35afb80cecd82d1a8d91b554022557e115f5c275f515','disconnected'),(9,'toto','test','9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08','disconnected'),(11,'test','ax','9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08','disconnected'),(13,'exemple','exemple','b77ad2edf199a4b4479347afaf387d435a12480d0dc5b8e042c4c8991587d080','disconnected');
/*!40000 ALTER TABLE `clients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messages` (
  `message_id` int NOT NULL AUTO_INCREMENT,
  `client_id` int NOT NULL,
  `salon_id` int NOT NULL,
  `contenu` text,
  `timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`message_id`),
  KEY `client_id` (`client_id`),
  KEY `salon_id` (`salon_id`),
  CONSTRAINT `messages_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `clients` (`client_id`),
  CONSTRAINT `messages_ibfk_2` FOREIGN KEY (`salon_id`) REFERENCES `salons` (`salon_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,13,1,' Bonjour !','2023-12-31 16:46:59'),(2,1,1,' Salut !','2023-12-31 16:47:05');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salons`
--

DROP TABLE IF EXISTS `salons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salons` (
  `salon_id` int NOT NULL AUTO_INCREMENT,
  `nom_salon` varchar(255) NOT NULL,
  PRIMARY KEY (`salon_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salons`
--

LOCK TABLES `salons` WRITE;
/*!40000 ALTER TABLE `salons` DISABLE KEYS */;
INSERT INTO `salons` VALUES (1,'Général'),(2,'Blabla'),(3,'Comptabilité'),(4,'Informatique'),(5,'Marketing');
/*!40000 ALTER TABLE `salons` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salons_adheres`
--

DROP TABLE IF EXISTS `salons_adheres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salons_adheres` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `salon_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `username` (`username`),
  KEY `salon_id` (`salon_id`),
  CONSTRAINT `salons_adheres_ibfk_1` FOREIGN KEY (`username`) REFERENCES `clients` (`username`),
  CONSTRAINT `salons_adheres_ibfk_2` FOREIGN KEY (`salon_id`) REFERENCES `salons` (`salon_id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salons_adheres`
--

LOCK TABLES `salons_adheres` WRITE;
/*!40000 ALTER TABLE `salons_adheres` DISABLE KEYS */;
INSERT INTO `salons_adheres` VALUES (1,'admin',1),(2,'admin',2),(3,'admin',3),(4,'admin',4),(5,'admin',5),(6,'toto',1),(7,'server',1),(18,'server',2),(19,'server',3),(20,'server',4),(21,'server',5),(23,'toto',2),(24,'toto',3),(25,'toto',4),(35,'toto',1),(41,'test',1),(43,'exemple',1),(44,'exemple',2),(45,'exemple',3);
/*!40000 ALTER TABLE `salons_adheres` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-31 22:11:03
