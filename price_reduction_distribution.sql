# 降价房源分布
SELECT
  SUM(today.total_price < yesterday.total_price)                  AS num,
  count(*)                                                        AS total,
  SUM(today.total_price < yesterday.total_price) / count(*) * 100 AS perc,
  area.name
FROM `20171228` today
  JOIN `20171227` yesterday ON today.house_id = yesterday.house_id
  JOIN area ON today.area_id = area.id
  JOIN location ON today.location_id = location.id
WHERE today.total_price < 1000 AND today.total_price > 600 AND
      today.layers > 6
GROUP BY today.area_id
ORDER BY perc DESC;