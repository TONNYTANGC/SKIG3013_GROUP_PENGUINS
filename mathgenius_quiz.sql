CREATE DATABASE  IF NOT EXISTS `mathgenius` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `mathgenius`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: mathgenius
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `quiz`
--

DROP TABLE IF EXISTS `quiz`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quiz` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `lesson` int NOT NULL,
  `subtopic` varchar(45) NOT NULL,
  `question` varchar(200) DEFAULT NULL,
  `srcQuesion` varchar(45) DEFAULT NULL,
  `optionA` varchar(200) NOT NULL,
  `optionB` varchar(200) NOT NULL,
  `optionC` varchar(200) NOT NULL,
  `optionD` varchar(200) NOT NULL,
  `correctOption` varchar(45) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quiz`
--

LOCK TABLES `quiz` WRITE;
/*!40000 ALTER TABLE `quiz` DISABLE KEYS */;
INSERT INTO `quiz` VALUES (1,1,'1','Apakah yang ditunjukkan oleh jarum pendek\npada jam analog?',NULL,'Jam','Minit','Saat','Detik','optionB'),(2,1,'1','Berapakah minit dalam satu pusingan lengkap jarum minit?',NULL,'15 minit','30 minit','45 minit','60 minit','optionD'),(3,1,'1','Berapakah jam dalam satu hari?',NULL,'10 jam','12 jam','24 jam','48 jam','optionC'),(4,1,'1',NULL,'static/img/quiz/clock-1.png','5:10','6:20','7:10',' 8:10','optionC'),(5,1,'1',NULL,'static/img/quiz/clock-2.png','Pukul satu setengah','Pukul dua setengah','Pukul tiga suku','Pukul enam setengah','optionB'),(6,1,'2','Apakah format utama dalam jam digital?',NULL,'Format 6 jam dan format 18 jam','Format 12 jam dan format 24 jam','Format 10 jam dan format 20 jam','Format 7 jam dan format 14 jam','optionB'),(7,1,'2',NULL,'static/img/quiz/clock-6.png','Jam lapan empat puluh minit','Jam tujuh dua puluh minit','Jam lima tiga puluh minit','Jam tujuh tiga puluh minit','optionD'),(8,1,'2','Bagaimanakah cara menukar jam 19:15 ke sistem jam 12?',NULL,'Tambahkan 12 jam','Tidak perlu melakukan perubahan','Kurangkan 12 jam','Tambahkan 24 jam','optionC'),(9,1,'2','Bagaimanakah cara menukar jam 10:40 A.M ke sistem jam 24?',NULL,'Tambahkan 12 jam','Tidak perlu melakukan perubahan','Kurangkan 12 jam','Tambahkan 24 jam','optionB'),(10,1,'2','Bagaimanakah cara membaca waktu 00:45 dalam',NULL,'Jam kosong empat puluh lima minit','Jam dua belas empat puluh lima minit pagi','Jam dua belas kurang lima belas minit malam','Jam dua belas lima puluh lima minit','optionB'),(11,1,'3','Jika Amir bermain selama 2 jam 15 minit, berapakah masa bermainnya dalam minit?',NULL,'120 minit','135 minit','150 minit','165 minit','optionB'),(12,1,'3','2 jam 30 minit - 1 jam 15 minit =',NULL,'1 jam 15 minit','1 jam 30 minit','1 jam 45 minit','2 jam','optionA'),(13,1,'3','1 jam 30 minit + 45 minit =',NULL,'2 jam 15 minit','2 jam 30 minit','2 jam 45 minit','3 jam','optionA'),(14,1,'3','4 jam x 3 =',NULL,'8 jam','10 jam','12 jam','15 jam','optionC'),(15,1,'3','Berapakah minit dalam 1 jam 45 minit?',NULL,'90 minit','105 minit','120 minit','135 minit','optionB'),(16,2,'1','Koin manakah yang mempunyai nilai paling rendah dalam sistem koin sen?',NULL,'5 sen','10 sen','20 sen','50 sen','optionA'),(17,2,'1','Koin 20 sen Malaysia biasanya mempamerkan gambar apa di permukaannya?',NULL,'Bunga Rafflesia','Burung Enggang','Bunga Melur','Pokok Kelapa','optionC'),(18,2,'1','Koin manakah yang mempunyai nilai paling tinggi dalam sistem koin sen?',NULL,'5 sen','10 sen','20 sen','50 sen','optionD'),(19,2,'1','Berapakah jumlah nilai koin tersebut jika anda mempunyai tiga keping koin 5 sen, dua keping koin 10 sen, dan satu keping koin 20 sen?',NULL,'45 sen','50 sen','55 sen','60 sen','optionC'),(20,2,'1','Jika kamu mempunyai 3 keping koin 10 sen dan 2 keping koin 20 sen, berapakah jumlah nilai wang yang kamu miliki?',NULL,'30 sen','40 sen','50 sen','70 sen','optionD'),(21,2,'2','Siapakah tokoh yang bergambar di dalam duit kertas Malaysia?',NULL,'Tunku Abdul Rahman','Sultan Abdul Samad','Tuanku Abdul Halim','Tun Abdul Razak','optionA'),(22,2,'2','Apakah yang menjadi gambar utama di dalam 1 ringgit Malaysia?',NULL,'Wau Bulan','Bunga Rafflesia','Pokok Getah','Harimau','optionA'),(23,2,'2','Apakah nilai tertinggi yang terdapat pada duit Malaysia sehingga terkini?',NULL,'50 ringgit','100 ringgit','200 ringgit','500 ringgit','optionB'),(24,2,'2','Duit kertas berwarna biru dengan gambar Wau Bulan adalah untuk nilai berapa ringgit?',NULL,'5 ringgit','10 ringgit','1 ringgit','50 ringgit','optionC'),(25,2,'2','Duit kertas RM50 dan RM20 masing-masing ada sebanyak 3 keping. Berapakah jumlah nilai keseluruhan kedua-dua jenis duit tersebut?',NULL,'RM90','RM120','RM150','RM210','optionD'),(26,2,'3','Berapa nilai dalam Ringgit Malaysia untuk 85 sen?',NULL,'RM 0.85 ','RM 8.50 ','RM 0.0085 ','RM 85 ','optionA'),(27,2,'3','Jika anda membeli tiga barang yang masing-masing berharga 60 sen, berapa jumlah yang perlu dibayar dalam Ringgit Malaysia?',NULL,'RM 0.18 ','RM 1.80 ','RM 180 ','RM 18 ','optionB'),(28,2,'3','Jika anda mempunyai 125 sen, berapakah nilai tersebut dalam Ringgit Malaysia?',NULL,'RM 1.25','RM 0.0125 ','RM 12.50','RM 125 ','optionA'),(29,2,'3','Anda membeli sebungkus kek seharga RM3.75 dan dua minuman seharga 60 sen setiap satu. Berapakah jumlah yang perlu dibayar?',NULL,'RM 4.95 ','RM 6.55 ','RM 7.10 ','RM 7.50 ','optionA'),(30,2,'3','Harga satu bungkus kudapan adalah 55 sen. Jika anda membeli 4 bungkus, berapakah jumlah yang perlu dibayar?',NULL,'110 sen','220 sen','240 sen','275 sen','optionB');
/*!40000 ALTER TABLE `quiz` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-17 21:15:57
