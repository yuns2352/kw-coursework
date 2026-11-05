SELECT d.driver_id,
       d.driver_name,
       COUNT(*) AS total_shipments
FROM Shipments AS s
JOIN Depots    AS dest ON dest.depot_code = s.dest_code
JOIN Customers AS c    ON c.customer_id = s.customer_id
JOIN Drivers   AS d    ON d.driver_id   = s.driver_id
WHERE YEAR(s.ship_date) = 2025
  AND dest.depot_country = '한국'
  AND c.customer_sector IN ('전자부품', '반도체')
GROUP BY d.driver_id, d.driver_name
ORDER BY total_shipments DESC, d.driver_id
LIMIT 5;