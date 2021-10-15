-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: cardealership-db.mysql.database.azure.com    Database: cardealership
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `car_part`
--

DROP TABLE IF EXISTS `car_part`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car_part` (
  `id` int NOT NULL AUTO_INCREMENT,
  `manufacturer_id` int NOT NULL,
  `weight` float DEFAULT NULL,
  `dimensions` varchar(45) DEFAULT NULL COMMENT 'HxWxD',
  `material` varchar(45) DEFAULT NULL,
  `eco_friendly` tinyint(1) DEFAULT NULL COMMENT 'yes/no',
  `vegan` tinyint(1) DEFAULT NULL COMMENT 'yes/no',
  `barcode` varchar(45) NOT NULL,
  `price` float DEFAULT '0',
  `serial_number` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`,`manufacturer_id`),
  KEY `fk_vehicle_part_manufacturer1_idx` (`manufacturer_id`),
  CONSTRAINT `fk_vehicle_part_manufacturer1` FOREIGN KEY (`manufacturer_id`) REFERENCES `manufacturer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `car_part_invoice_line`
--

DROP TABLE IF EXISTS `car_part_invoice_line`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car_part_invoice_line` (
  `invoice_id` int NOT NULL,
  `car_part_id` int NOT NULL,
  `quantity` int DEFAULT '1',
  PRIMARY KEY (`invoice_id`,`car_part_id`),
  KEY `fk_invoice_has_car_part_car_part1_idx` (`car_part_id`),
  KEY `fk_invoice_has_car_part_invoice1_idx` (`invoice_id`),
  CONSTRAINT `fk_invoice_has_car_part_car_part1` FOREIGN KEY (`car_part_id`) REFERENCES `car_part` (`id`),
  CONSTRAINT `fk_invoice_has_car_part_invoice1` FOREIGN KEY (`invoice_id`) REFERENCES `invoice` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `firstname` varchar(20) NOT NULL,
  `lastname` varchar(45) NOT NULL,
  `email` varchar(55) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `postcode` int NOT NULL,
  `address` varchar(45) NOT NULL,
  `password` varchar(100) NOT NULL,
  `timestamp` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  KEY `fk_customer_location1_idx` (`postcode`),
  CONSTRAINT `customer_location_postcode_fk` FOREIGN KEY (`postcode`) REFERENCES `location` (`postcode`)
) ENGINE=InnoDB AUTO_INCREMENT=347 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `customer_vehicle`
--

DROP TABLE IF EXISTS `customer_vehicle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_vehicle` (
  `vehicle_ident_number` varchar(17) NOT NULL,
  `customer_id` int NOT NULL,
  `vehicle_id` int NOT NULL,
  `license_plate` varchar(10) NOT NULL,
  PRIMARY KEY (`vehicle_ident_number`,`customer_id`,`vehicle_id`),
  UNIQUE KEY `license_plate_UNIQUE` (`license_plate`),
  KEY `fk_customer_has_vehicle_vehicle1_idx` (`vehicle_id`),
  KEY `fk_customer_has_vehicle_customer1_idx` (`customer_id`),
  CONSTRAINT `fk_customer_has_vehicle_customer1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`),
  CONSTRAINT `fk_customer_has_vehicle_vehicle1` FOREIGN KEY (`vehicle_id`) REFERENCES `vehicle` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dealership`
--

DROP TABLE IF EXISTS `dealership`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dealership` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `postcode` int NOT NULL,
  `address` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dealership_location_postcode_fk` (`postcode`),
  CONSTRAINT `dealership_location_postcode_fk` FOREIGN KEY (`postcode`) REFERENCES `location` (`postcode`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `dealership_parts_inventory`
--

DROP TABLE IF EXISTS `dealership_parts_inventory`;
/*!50001 DROP VIEW IF EXISTS `dealership_parts_inventory`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `dealership_parts_inventory` AS SELECT 
 1 AS `id`,
 1 AS `brand`,
 1 AS `weight`,
 1 AS `dimensions`,
 1 AS `material`,
 1 AS `barcode`,
 1 AS `serial_number`,
 1 AS `quantity`,
 1 AS `price per unit`,
 1 AS `dealership`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `dealership_service`
--

DROP TABLE IF EXISTS `dealership_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dealership_service` (
  `dealership_id` int NOT NULL,
  `service_catalog_id` int NOT NULL,
  PRIMARY KEY (`service_catalog_id`,`dealership_id`),
  KEY `fk_dealership_has_service_catalog_service_catalog1_idx` (`service_catalog_id`),
  KEY `fk_dealership_has_service_catalog_dealership1_idx` (`dealership_id`),
  CONSTRAINT `fk_dealership_has_service_catalog_dealership1` FOREIGN KEY (`dealership_id`) REFERENCES `dealership` (`id`),
  CONSTRAINT `fk_dealership_has_service_catalog_service_catalog1` FOREIGN KEY (`service_catalog_id`) REFERENCES `service_catalog` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `dealership_services`
--

DROP TABLE IF EXISTS `dealership_services`;
/*!50001 DROP VIEW IF EXISTS `dealership_services`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `dealership_services` AS SELECT 
 1 AS `dealership`,
 1 AS `service_type`,
 1 AS `price`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `dealership_vehicle_inventory`
--

DROP TABLE IF EXISTS `dealership_vehicle_inventory`;
/*!50001 DROP VIEW IF EXISTS `dealership_vehicle_inventory`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `dealership_vehicle_inventory` AS SELECT 
 1 AS `id`,
 1 AS `model`,
 1 AS `year`,
 1 AS `brand`,
 1 AS `dealership`,
 1 AS `price per unit`,
 1 AS `quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `id` int NOT NULL AUTO_INCREMENT,
  `dealership_id` int NOT NULL,
  `postcode` int NOT NULL COMMENT 'The city the employee lives in.',
  `department_id` int NOT NULL,
  `firstname` varchar(45) NOT NULL,
  `lastname` varchar(45) NOT NULL,
  `email` varchar(55) NOT NULL,
  `address` varchar(45) NOT NULL,
  `position` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_employee_dealership_idx` (`dealership_id`),
  KEY `fk_employee_department1_idx` (`department_id`),
  KEY `employee_location_postcode_fk` (`postcode`),
  CONSTRAINT `employee_location_postcode_fk` FOREIGN KEY (`postcode`) REFERENCES `location` (`postcode`),
  CONSTRAINT `fk_employee_dealership` FOREIGN KEY (`dealership_id`) REFERENCES `dealership` (`id`),
  CONSTRAINT `fk_employee_department1` FOREIGN KEY (`department_id`) REFERENCES `department` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=152 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `invoice`
--

DROP TABLE IF EXISTS `invoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invoice` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int NOT NULL,
  `dealership_id` int NOT NULL,
  `total_cost` int DEFAULT NULL,
  `timestamp` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_invoice_customer1_idx` (`customer_id`),
  KEY `fk_invoice_dealership1_idx` (`dealership_id`),
  CONSTRAINT `fk_invoice_customer1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`),
  CONSTRAINT `fk_invoice_dealership1` FOREIGN KEY (`dealership_id`) REFERENCES `dealership` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `invoice_details`
--

DROP TABLE IF EXISTS `invoice_details`;
/*!50001 DROP VIEW IF EXISTS `invoice_details`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `invoice_details` AS SELECT 
 1 AS `id`,
 1 AS `customer_id`,
 1 AS `dealership_id`,
 1 AS `total_cost`,
 1 AS `timestamp`,
 1 AS `invoice_id`,
 1 AS `vehicle_id`,
 1 AS `quantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `location` (
  `postcode` int NOT NULL,
  `city` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`postcode`),
  UNIQUE KEY `postcode_UNIQUE` (`postcode`),
  UNIQUE KEY `city_UNIQUE` (`city`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `manufacturer`
--

DROP TABLE IF EXISTS `manufacturer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manufacturer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `company_name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `company_name_UNIQUE` (`company_name`) /*!80000 INVISIBLE */
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `part_inventory`
--

DROP TABLE IF EXISTS `part_inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `part_inventory` (
  `dealership_id` int NOT NULL,
  `car_part_id` int NOT NULL,
  `quantity` int DEFAULT '0',
  PRIMARY KEY (`car_part_id`,`dealership_id`),
  KEY `fk_vehicle_has_dealership_dealership1_idx` (`dealership_id`),
  KEY `fk_vehicle_has_dealership_car_part1_idx` (`car_part_id`),
  CONSTRAINT `fk_vehicle_has_dealership_car_part1` FOREIGN KEY (`car_part_id`) REFERENCES `car_part` (`id`),
  CONSTRAINT `fk_vehicle_has_dealership_dealership1` FOREIGN KEY (`dealership_id`) REFERENCES `dealership` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `service_catalog`
--

DROP TABLE IF EXISTS `service_catalog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `service_catalog` (
  `id` int NOT NULL AUTO_INCREMENT,
  `service_type` varchar(55) DEFAULT NULL,
  `price` float DEFAULT '0',
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `service_type_UNIQUE` (`service_type`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `service_request`
--

DROP TABLE IF EXISTS `service_request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `service_request` (
  `id` int NOT NULL AUTO_INCREMENT,
  `vehicle_ident_number` varchar(17) NOT NULL,
  `service_catalog_id` int NOT NULL,
  `mechanic` int NOT NULL,
  `service_date` date DEFAULT NULL,
  `date_added` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `service_request_service_catalog_id_fk` (`service_catalog_id`),
  KEY `service_request_employee_id_fk` (`mechanic`),
  KEY `service_request_customer_vehicle_vehicle_ident_number_fk_idx` (`vehicle_ident_number`),
  CONSTRAINT `service_request_customer_vehicle_vehicle_ident_number_fk` FOREIGN KEY (`vehicle_ident_number`) REFERENCES `customer_vehicle` (`vehicle_ident_number`),
  CONSTRAINT `service_request_employee_id_fk` FOREIGN KEY (`mechanic`) REFERENCES `employee` (`id`),
  CONSTRAINT `service_request_service_catalog_id_fk` FOREIGN KEY (`service_catalog_id`) REFERENCES `service_catalog` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8 COMMENT='The dealership + customer is pulled through the mechanic and vehicle_ident_number respectively';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `service_request_invoice_line`
--

DROP TABLE IF EXISTS `service_request_invoice_line`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `service_request_invoice_line` (
  `invoice_id` int NOT NULL,
  `service_request_id` int NOT NULL,
  `quantity` int DEFAULT '1',
  PRIMARY KEY (`invoice_id`,`service_request_id`),
  KEY `fk_service_request_has_invoice_invoice1_idx` (`invoice_id`),
  KEY `fk_service_request_has_invoice_service_request1_idx` (`service_request_id`),
  CONSTRAINT `fk_service_request_has_invoice_invoice1` FOREIGN KEY (`invoice_id`) REFERENCES `invoice` (`id`),
  CONSTRAINT `fk_service_request_has_invoice_service_request1` FOREIGN KEY (`service_request_id`) REFERENCES `service_request` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `vehicle`
--

DROP TABLE IF EXISTS `vehicle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicle` (
  `id` int NOT NULL AUTO_INCREMENT,
  `manufacturer_id` int NOT NULL,
  `model` varchar(45) DEFAULT NULL,
  `year` int DEFAULT NULL,
  `price` float DEFAULT '0',
  `top_speed` varchar(10) DEFAULT NULL,
  `fuel_type` varchar(10) DEFAULT NULL,
  `fuel_consumption` varchar(10) DEFAULT NULL,
  `co2_emission` varchar(10) DEFAULT NULL,
  `width_cm` int DEFAULT NULL,
  `height_cm` int DEFAULT NULL,
  `length_cm` int DEFAULT NULL,
  `load_capacity_kg` int DEFAULT NULL,
  `cylinder` int DEFAULT NULL,
  `abs` tinyint(1) DEFAULT NULL,
  `airbag` int DEFAULT NULL,
  `tank_capacity` int DEFAULT NULL,
  `gear` varchar(10) DEFAULT NULL,
  `gear_type` int DEFAULT NULL,
  `weight_kg` int DEFAULT NULL,
  `door` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`,`manufacturer_id`),
  KEY `fk_vehicle_manufacturer1_idx` (`manufacturer_id`),
  CONSTRAINT `fk_vehicle_manufacturer1` FOREIGN KEY (`manufacturer_id`) REFERENCES `manufacturer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=390 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `vehicle_inventory`
--

DROP TABLE IF EXISTS `vehicle_inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicle_inventory` (
  `vehicle_id` int NOT NULL,
  `dealership_id` int NOT NULL,
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`vehicle_id`,`dealership_id`),
  KEY `fk_vehicle_has_dealership_dealership2_idx` (`dealership_id`),
  KEY `fk_vehicle_has_dealership_vehicle1_idx` (`vehicle_id`),
  CONSTRAINT `fk_vehicle_has_dealership_dealership2` FOREIGN KEY (`dealership_id`) REFERENCES `dealership` (`id`),
  CONSTRAINT `fk_vehicle_has_dealership_vehicle1` FOREIGN KEY (`vehicle_id`) REFERENCES `vehicle` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `vehicle_invoice_line`
--

DROP TABLE IF EXISTS `vehicle_invoice_line`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicle_invoice_line` (
  `invoice_id` int NOT NULL,
  `vehicle_id` int NOT NULL,
  `quantity` int DEFAULT '1',
  PRIMARY KEY (`invoice_id`,`vehicle_id`),
  KEY `fk_vehicle_has_invoice_invoice1_idx` (`invoice_id`),
  KEY `fk_vehicle_has_invoice_vehicle1_idx` (`vehicle_id`),
  CONSTRAINT `fk_vehicle_has_invoice_invoice1` FOREIGN KEY (`invoice_id`) REFERENCES `invoice` (`id`),
  CONSTRAINT `fk_vehicle_has_invoice_vehicle1` FOREIGN KEY (`vehicle_id`) REFERENCES `vehicle` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Final view structure for view `dealership_parts_inventory`
--

/*!50001 DROP VIEW IF EXISTS `dealership_parts_inventory`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`cardealershipadmin`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `dealership_parts_inventory` AS select `car_part`.`id` AS `id`,`m`.`company_name` AS `brand`,`car_part`.`weight` AS `weight`,`car_part`.`dimensions` AS `dimensions`,`car_part`.`material` AS `material`,`car_part`.`barcode` AS `barcode`,`car_part`.`serial_number` AS `serial_number`,`pi`.`quantity` AS `quantity`,`car_part`.`price` AS `price per unit`,`d`.`name` AS `dealership` from (((`car_part` join `part_inventory` `pi` on((`car_part`.`id` = `pi`.`car_part_id`))) join `dealership` `d` on((`pi`.`dealership_id` = `d`.`id`))) join `manufacturer` `m` on((`car_part`.`manufacturer_id` = `m`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `dealership_services`
--

/*!50001 DROP VIEW IF EXISTS `dealership_services`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`cardealershipadmin`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `dealership_services` AS select `d`.`name` AS `dealership`,`service_catalog`.`service_type` AS `service_type`,`service_catalog`.`price` AS `price` from ((`service_catalog` join `dealership_service` `ds` on((`service_catalog`.`id` = `ds`.`service_catalog_id`))) join `dealership` `d` on((`d`.`id` = `ds`.`dealership_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `dealership_vehicle_inventory`
--

/*!50001 DROP VIEW IF EXISTS `dealership_vehicle_inventory`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`cardealershipadmin`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `dealership_vehicle_inventory` AS select `vehicle`.`id` AS `id`,`vehicle`.`model` AS `model`,`vehicle`.`year` AS `year`,`m`.`company_name` AS `brand`,`d`.`name` AS `dealership`,`vehicle`.`price` AS `price per unit`,`vi`.`quantity` AS `quantity` from (((`vehicle` join `vehicle_inventory` `vi` on((`vehicle`.`id` = `vi`.`vehicle_id`))) join `dealership` `d` on((`d`.`id` = `vi`.`dealership_id`))) join `manufacturer` `m` on((`vehicle`.`manufacturer_id` = `m`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `invoice_details`
--

/*!50001 DROP VIEW IF EXISTS `invoice_details`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`cardealershipadmin`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `invoice_details` AS select `i`.`id` AS `id`,`i`.`customer_id` AS `customer_id`,`i`.`dealership_id` AS `dealership_id`,`i`.`total_cost` AS `total_cost`,`i`.`timestamp` AS `timestamp`,`vil`.`invoice_id` AS `invoice_id`,`vil`.`vehicle_id` AS `vehicle_id`,`vil`.`quantity` AS `quantity` from (`invoice` `i` left join `vehicle_invoice_line` `vil` on((`i`.`id` = `vil`.`invoice_id`))) union select `i`.`id` AS `id`,`i`.`customer_id` AS `customer_id`,`i`.`dealership_id` AS `dealership_id`,`i`.`total_cost` AS `total_cost`,`i`.`timestamp` AS `timestamp`,`cpil`.`invoice_id` AS `invoice_id`,`cpil`.`car_part_id` AS `car_part_id`,`cpil`.`quantity` AS `quantity` from (`invoice` `i` left join `car_part_invoice_line` `cpil` on((`i`.`id` = `cpil`.`invoice_id`))) union select `i`.`id` AS `id`,`i`.`customer_id` AS `customer_id`,`i`.`dealership_id` AS `dealership_id`,`i`.`total_cost` AS `total_cost`,`i`.`timestamp` AS `timestamp`,`sril`.`invoice_id` AS `invoice_id`,`sril`.`service_request_id` AS `service_request_id`,`sril`.`quantity` AS `quantity` from (`invoice` `i` left join `service_request_invoice_line` `sril` on((`i`.`id` = `sril`.`invoice_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-15  8:51:01
