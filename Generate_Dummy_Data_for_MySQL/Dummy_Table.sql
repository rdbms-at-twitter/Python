CREATE TABLE `Dummy_Table` (
 `id` bigint unsigned NOT NULL AUTO_INCREMENT,
 `uid` varchar(255) NOT NULL,
 `cid` tinyint unsigned NOT NULL,
 `cfname` varchar(255) NOT NULL,
 `clname` varchar(255) NOT NULL,
 `description` text NOT NULL,
 `flag_id` tinyint NOT NULL DEFAULT '0',
 `created` datetime(6) NOT NULL,
 PRIMARY KEY (`id`),
 UNIQUE KEY `user_id` (`uid`),
 KEY `idx_created` (`created`),
 KEY `idx_flag_id` (`flag_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4
