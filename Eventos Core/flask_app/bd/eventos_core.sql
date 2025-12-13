-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: localhost    Database: eventos_core
-- ------------------------------------------------------
-- Server version	8.0.44

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
-- Table structure for table `eventos`
--

DROP TABLE IF EXISTS `eventos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eventos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `evento` varchar(255) DEFAULT NULL,
  `ubicacion` varchar(255) DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  `descripcion` text,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `usuario_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_eventos_usuarios_idx` (`usuario_id`),
  CONSTRAINT `fk_eventos_usuarios` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eventos`
--

LOCK TABLES `eventos` WRITE;
/*!40000 ALTER TABLE `eventos` DISABLE KEYS */;
INSERT INTO `eventos` VALUES (2,'ir a la playa','chinchorro','2026-01-23 00:00:00','vamos a la playa oh-oh-oh','2025-12-12 01:18:05','2025-12-12 01:18:05',2),(3,'Viaje a tacna','Peru','2026-02-13 00:00:00','Viajando a tacna he hilo Peru','2025-12-12 11:48:38','2025-12-12 11:48:38',2),(4,'Firma shek','muy muy lejano ','2025-12-11 00:00:00','FIIIIIIIIIRMAAAA','2025-12-12 17:25:14','2025-12-13 01:49:54',1),(5,'Juego de Futbol','Canchas del parque ','2024-03-30 00:00:00','Juego amistoso de futbol. Todos están invitados a participar y animarnos en el juego. Se harán de manera regular cada 3 semanas','2025-12-13 00:47:23','2025-12-13 00:47:23',4),(6,'Clases de cocina ','Restaurante Sol','2024-04-01 00:00:00','Clases de cocina con la chef Andrea. Aprenderemos a preparar platillos como “Asado de boda”','2025-12-13 00:49:52','2025-12-13 00:49:52',5),(7,'Competencia de Karate','Dojo','2024-04-15 00:00:00','Bienvenidos a la competencia de karate anual de la academia \"manos de acero\"','2025-12-13 00:52:29','2025-12-13 00:52:29',6),(8,'Degustación de tacos','Taquería Juarez','2024-04-30 00:00:00','Estan todos invitados a participar en la degustacion de la taqueria Juarez, Nos vemos pronto ','2025-12-13 00:54:20','2025-12-13 00:54:20',5);
/*!40000 ALTER TABLE `eventos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `apellido` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Jorge','Vargas','jvargasq1996@gmail.com','$2b$12$c6f8eVaYVn/9PRvZYe2Rb.lCjrA5cDodNQcdxfEoQqViWyU9rtlx6','2025-12-11 23:47:19','2025-12-11 23:47:19'),(2,'damaris','vargas','dama@gmail.com','$2b$12$0P0W12I/t9v3DYvtD8sWDeQyBPxi7647xdrPMcFTZ4KqX2fw3nbIW','2025-12-12 01:17:31','2025-12-12 01:17:31'),(3,'alejandra','quispe','alita@gmail.com','$2b$12$w0BJnQw1dGlWs5KMIxNPY.gxDCDJFlCwiURgO5Sk5bWDZeFmvNcz2','2025-12-12 01:24:37','2025-12-12 01:24:37'),(4,'Patricio','Valdez','patricio@gmail.com','$2b$12$7LJi326p3bd07HpAuvjXEujo/0v3xk2CAGVKGSbtqj9q5iNu2F3.2','2025-12-13 00:36:40','2025-12-13 00:36:40'),(5,'Andrea','Villanueva','andrea@gmail.com','$2b$12$nMjBfRnzBn5cB1NFqJnpFO8O2vFKrZz6ZHolyFBNhPYJ5HktVfvqe','2025-12-13 00:47:58','2025-12-13 00:47:58'),(6,'Miyagi','Katana','miyagi@gmail.com','$2b$12$JkPMThIXT00W14mWxv/o3ub9aFv5KqYwu2mlG4wIPLiDCKY2svqD6','2025-12-13 00:51:37','2025-12-13 00:51:37');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-13  2:32:59
