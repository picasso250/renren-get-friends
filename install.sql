delimiter $$

CREATE TABLE `relation` (
  `s1` int(10) unsigned NOT NULL DEFAULT '0',
  `s2` int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`s1`,`s2`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8$$


delimiter $$

CREATE TABLE `student` (
  `uid` int(10) unsigned NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `uni_id` varchar(45) DEFAULT NULL,
  `college_id` int(10) unsigned DEFAULT NULL,
  `college_year` year(4) DEFAULT NULL,
  `star` tinyint(4) DEFAULT NULL,
  `avatar` varchar(255) DEFAULT NULL,
  `has_visit` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `is_private` tinyint(3) unsigned DEFAULT NULL,
  `high_school_id` int(10) unsigned DEFAULT NULL,
  `high_school_year` year(4) DEFAULT NULL,
  `has_visit_info` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `is_in_love` varchar(45) DEFAULT NULL COMMENT '感情状态',
  `mobile` varchar(45) DEFAULT NULL,
  `msn` varchar(45) DEFAULT NULL,
  `website` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8$$


delimiter $$

CREATE TABLE `school` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `uid` int(10) unsigned DEFAULT NULL,
  `info` varchar(255) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8$$

delimiter $$

CREATE TABLE `company` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `uid` int(10) unsigned DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `time_range` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8$$

