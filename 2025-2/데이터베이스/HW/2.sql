SELECT s.shipment_id, s.customer_id, s.ship_date
FROM Shipments AS s
JOIN Depots AS o ON o.depot_code = s.origin_code  
JOIN Depots AS d ON d.depot_code = s.dest_code     
WHERE s.ship_date BETWEEN '2025-01-01' AND '2025-05-31'
  AND o.depot_country = '미국'
  AND d.depot_country = '한국'
ORDER BY s.ship_date ASC;