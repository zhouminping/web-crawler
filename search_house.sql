# 徐汇(4): 漕河泾(69), 衡山路(73), 建国西路(74), 田林(78), 万体馆(79), 徐家汇(81), 斜土路(82)
# 普陀(5): 长风(84), 长寿路(85), 曹杨(86), 武宁(92), 中远两湾城(95)
# 长宁(7): 古北(105), 天山(107), 中山公园(112), 镇宁路(111), 仙霞(110)
# 黄浦(10)
# 静安(11)
USE house_info;

SELECT
  `20171224`.*,
  area.name,
  location.name
FROM `20171226` house
  JOIN area ON `20171224`.area_id = area.id
  JOIN location ON `20171224`.location_id = location.id
WHERE (`20171224`.area_id IN (10, 11)
       OR location_id IN (73, 74, 79, 81, 84, 85, 86, 92, 105, 107, 112, 110, 111))
      AND total_price > 600 AND total_price < 900
      AND layers > 7 AND size > 80 AND age > 1997 AND floor != '低区'
INTO OUTFILE '/root/data/result.csv'
FIELDS TERMINATED BY ',';