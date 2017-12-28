CREATE TABLE IF NOT EXISTS `20171228`
(
  id             INT(10) UNSIGNED AUTO_INCREMENT,
  house_id       BIGINT UNSIGNED UNIQUE NOT NULL,
  href           VARCHAR(255),
  area_id        INT(10) UNSIGNED,
  location_id    INT(10) UNSIGNED,
  community      VARCHAR(255),
  age            INT(10) UNSIGNED,
  size           FLOAT UNSIGNED,
  layers         INT(10) UNSIGNED,
  floor          VARCHAR(255),
  facing         VARCHAR(255),
  decorate       VARCHAR(255),
  buy_time       VARCHAR(255),
  years          VARCHAR(255),
  unit_price     INT(10) UNSIGNED,
  total_price    INT(10) UNSIGNED,
  7_days_watch   INT(10) UNSIGNED,
  total_watch    INT(10) UNSIGNED,
  first_visit    VARCHAR(255),
  PRIMARY KEY (`id`),
  FOREIGN KEY (`location_id`) REFERENCES location (`id`),
  FOREIGN KEY (`area_id`) REFERENCES area (`id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;