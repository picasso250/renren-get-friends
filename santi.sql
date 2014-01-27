
-- ----------------------------
-- Table structure for scene
-- ----------------------------
DROP TABLE IF EXISTS `scene`;
CREATE TABLE `scene` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `number` varchar(10) DEFAULT NULL,
  `number_extra` char(6) DEFAULT NULL,
  `text` text,
  `img` varchar(255) DEFAULT NULL,
  `is_delete` tinyint(1) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
