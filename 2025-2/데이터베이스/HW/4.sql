SELECT k.depot_code,
       COUNT(s.shipment_id)              AS shipments_to_korea,
       COUNT(DISTINCT s.customer_id)     AS distinct_customers
FROM Depots AS k
LEFT JOIN Shipments AS s
  ON s.dest_code = k.depot_code         
WHERE k.depot_country = '한국'
GROUP BY k.depot_code
ORDER BY k.depot_code;