 CREATE TABLE `t_feed` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(1024) DEFAULT NULL,
  `link` varchar(2048) DEFAULT NULL,
  `description` text NOT NULL,
  `summary` text NOT NULL,
  `modify_user` varchar(255) NOT NULL DEFAULT (current_user()),
  `updated_time` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_update_time` (`updated_time`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
