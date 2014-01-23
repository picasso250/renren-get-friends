delimiter $$

CREATE TABLE `relation` (
  `s1` int(10) unsigned NOT NULL DEFAULT '0',
  `s2` int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`s1`,`s2`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8$$



CREATE TABLE `student` (
  `uid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `school_name` varchar(45) DEFAULT NULL,
  `star` tinyint(4) DEFAULT NULL,
  `avatar` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8$$

