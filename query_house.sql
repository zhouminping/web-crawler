USE house_info;

CREATE TABLE IF NOT EXISTS `area` (
  `id`   INT UNSIGNED AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `href` VARCHAR(255),
  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

CREATE TABLE IF NOT EXISTS `location` (
  `id`      INT UNSIGNED AUTO_INCREMENT,
  `name`    VARCHAR(255) NOT NULL,
  `href`    VARCHAR(255),
  `area_id` INT UNSIGNED,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`area_id`) REFERENCES area (`id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

CREATE TABLE IF NOT EXISTS `house` (
  `id`          INT UNSIGNED AUTO_INCREMENT,
  `house_id`    BIGINT UNSIGNED UNIQUE NOT NULL,
  `community`   VARCHAR(255),
  `age`         INT UNSIGNED,
  `size`        FLOAT UNSIGNED,
  `layers`      INT UNSIGNED,
  `floor`       VARCHAR(255),
  `orientation` VARCHAR(255),
  `five_years`  BOOLEAN,
  `two_years`   BOOLEAN,
  `unit_price`  INT UNSIGNED,
  `total_price` INT UNSIGNED,
  `location_id` INT UNSIGNED,
  `area_id`     INT UNSIGNED,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`location_id`) REFERENCES location (`id`),
  FOREIGN KEY (`area_id`) REFERENCES area (`id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;


CREATE TABLE IF NOT EXISTS `20171227`
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
  `7_days_watch` INT(10) UNSIGNED,
  total_watch    INT(10) UNSIGNED,
  first_visit    VARCHAR(255),
  PRIMARY KEY (`id`),
  FOREIGN KEY (`location_id`) REFERENCES location (`id`),
  FOREIGN KEY (`area_id`) REFERENCES area (`id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8;


DELETE FROM `area`
WHERE id > 0;
DELETE FROM `location`
WHERE id > 0;
ALTER TABLE `area`
  AUTO_INCREMENT = 1;
ALTER TABLE `location`
  AUTO_INCREMENT = 1;


DELETE FROM `20171225`
WHERE id > 0;
ALTER TABLE `20171225`
  AUTO_INCREMENT = 1;

DELETE FROM `test`
WHERE id > 0;
ALTER TABLE `test`
  AUTO_INCREMENT = 1;

SELECT
  area.name,
  location.name,
  SUM(`20171224`.years LIKE '满二')                  AS 'number',
  count(1)                                         AS total,
  SUM(`20171224`.years LIKE '满二') * 100 / count(1) AS percentage
FROM `20171224`
  JOIN area ON `20171224`.area_id = area.id
  JOIN location ON `20171224`.location_id = location.id
GROUP BY area.id, location.id;

SELECT
  `20171224`.href,
  `20171224`.community,
  `20171224`.age,
  `20171224`.size,
  `20171224`.layers,
  `20171224`.floor,
  `20171224`.facing,
  `20171224`.decorate,
  `20171224`.buy_time,
  `20171224`.years,
  `20171224`.unit_price,
  `20171224`.total_price,
  `20171224`.`7_days_watch`,
  `20171224`.total_watch,
  `20171224`.first_visit,
  area.name,
  location.name,
  unit_price / comm_avg.avg * 100 AS perc
FROM `20171224`
  JOIN area ON `20171224`.area_id = area.id
  JOIN location ON `20171224`.location_id = location.id
  JOIN
  (SELECT
     round(avg(unit_price), 2) AS avg,
     community                 AS commumity
   FROM `20171224`
   WHERE area_id IN (4, 5, 7, 11)
   GROUP BY community) AS comm_avg
    ON community = comm_avg.commumity
WHERE unit_price / comm_avg.avg < 0.85 AND total_price < 1000 AND total_price > 600 AND layers > 6 AND age != 0;


SELECT count(1)
FROM `20171225`;

SELECT count(1)
FROM `20171224`;

# 新上房源
SELECT
  today.*,
  area.name,
  location.name
FROM `20171227` today
  JOIN area ON today.area_id = area.id
  JOIN location ON today.location_id = location.id
WHERE today.house_id NOT IN
      (SELECT yesterday.house_id
       FROM `20171226` yesterday)
      AND today.area_id IN (4, 5, 7, 11);

# 新上房源
SELECT
  count(*),
  area.name,
  location.name
FROM `20171227` today
  JOIN area ON today.area_id = area.id
  JOIN location ON today.location_id = location.id
WHERE today.house_id NOT IN
      (SELECT yesterday.house_id
       FROM `20171226` yesterday)
      AND today.area_id IN (4, 5, 7, 11)
GROUP BY today.area_id, today.location_id;

SELECT count(*)
FROM `20171226` today
WHERE today.house_id NOT IN
      (SELECT yesterday.house_id
       FROM `20171225` yesterday)
      AND today.area_id IN (4, 5, 7, 11);

# 新上未满二或满二房源
SELECT SUM(today.years LIKE '%满二') AS count
FROM `20171226` today
WHERE today.house_id NOT IN
      (SELECT yesterday.house_id
       FROM `20171225` yesterday)
      AND today.area_id IN (4, 5, 7, 11);

# 下架房源
SELECT
  count(*),
  area.name,
  location.name
FROM `20171226` yesterday
  JOIN area ON yesterday.area_id = area.id
  JOIN location ON yesterday.location_id = location.id
WHERE yesterday.house_id NOT IN
      (SELECT today.house_id
       FROM `20171227` today)
      AND yesterday.area_id IN (4, 5, 7, 11)
GROUP BY yesterday.area_id, yesterday.location_id;

# 下架房源
SELECT
  yesterday.*,
  area.name,
  location.name
FROM `20171226` yesterday
  JOIN area ON yesterday.area_id = area.id
  JOIN location ON yesterday.location_id = location.id
WHERE yesterday.house_id NOT IN
      (SELECT today.house_id
       FROM `20171227` today)
      AND yesterday.area_id IN (4, 5, 7, 11);

SELECT count(*)
FROM `20171225` yesterday
WHERE yesterday.house_id NOT IN
      (SELECT today.house_id
       FROM `20171226` today)
      AND yesterday.area_id IN (4, 5, 7, 11);

SELECT SUM(yesterday.years LIKE '%满二') AS count
FROM `20171225` yesterday
WHERE yesterday.house_id NOT IN
      (SELECT today.house_id
       FROM `20171226` today)
      AND yesterday.area_id IN (4, 5, 7, 11);

# 降价房源
SELECT
  today.*,
  area.name,
  location.name,
  (yesterday.total_price - today.total_price) / yesterday.total_price * 100 AS perc
FROM `20171228` today
  JOIN `20171227` yesterday ON today.house_id = yesterday.house_id
  JOIN area ON today.area_id = area.id
  JOIN location ON today.location_id = location.id
WHERE today.total_price < yesterday.total_price
      AND today.total_price < 1000 AND today.total_price > 600 AND
      today.layers > 6 AND today.area_id IN (4, 5, 7, 10, 11);

# 降价房源
SELECT
  SUM(today.total_price < yesterday.total_price)                  AS num,
  count(*)                                                        AS total,
  SUM(today.total_price < yesterday.total_price) / count(*) * 100 AS perc,
  area.name
FROM `20171226` today
  JOIN `20171225` yesterday ON today.house_id = yesterday.house_id
  JOIN area ON today.area_id = area.id
  JOIN location ON today.location_id = location.id
WHERE today.total_price < 1000 AND today.total_price > 600 AND
      today.layers > 6
GROUP BY today.area_id
ORDER BY perc DESC;

# 涨价房源
SELECT
  SUM(today.total_price > yesterday.total_price)                  AS num,
  count(*)                                                        AS total,
  SUM(today.total_price > yesterday.total_price) / count(*) * 100 AS perc,
  area.name
FROM `20171226` today
  JOIN `20171225` yesterday ON today.house_id = yesterday.house_id
  JOIN area ON today.area_id = area.id
  JOIN location ON today.location_id = location.id
GROUP BY today.area_id;

SELECT
  today.*,
  area.name,
  location.name,
  (today.total_price - yesterday.total_price) / yesterday.total_price * 100 AS perc
FROM `20171228` today
  JOIN `20171227` yesterday ON today.house_id = yesterday.house_id
  JOIN area ON today.area_id = area.id
  JOIN location ON today.location_id = location.id
WHERE today.total_price > yesterday.total_price AND today.total_price < 1000 AND today.total_price > 600 AND
      today.layers > 6 AND today.area_id IN (4, 5, 7, 11);


SELECT *
FROM `20171226`
WHERE area_id IN (4, 5, 7, 11) AND first_visit IS NOT NULL AND first_visit != ''
ORDER BY first_visit ASC
LIMIT 100;

SELECT
  house.*,
  area.name,
  location.name
FROM `20171228` house
  JOIN area ON house.area_id = area.id
  JOIN location ON house.location_id = location.id
WHERE total_price < 1000 AND total_price > 600 AND
      layers > 6 AND size > 85 AND house.area_id IN (4, 5, 7, 10, 11)
ORDER BY total_watch DESC
LIMIT 100;

