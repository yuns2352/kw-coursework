SELECT s.shipment_id,
       o.depot_country AS origin_country,
       d.depot_country AS dest_country,
       s.ship_date
FROM Shipments AS s
JOIN Depots AS o ON o.depot_code = s.origin_code
JOIN Depots AS d ON d.depot_code = s.dest_code
WHERE (
        s.ship_date BETWEEN '2025-01-01' AND '2025-03-31'
        AND d.depot_country = '한국'
      )
   OR (
        s.ship_date BETWEEN '2025-04-01' AND '2025-06-30'
        AND d.depot_country = '미국'
      )
ORDER BY s.ship_date ASC, s.shipment_id;