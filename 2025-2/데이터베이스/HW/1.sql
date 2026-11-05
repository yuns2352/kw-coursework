SELECT DISTINCT s.ship_id
FROM Shipments AS s
JOIN Drivers AS d ON d.driver_id = s.driver_id
WHERE d.driver_age < 35;