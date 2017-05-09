SELECT DISTINCT o.nr, o.price FROM offer o, vendor v WHERE o.product=1 AND o."deliveryDays"<=3 AND v.country='US' AND o."validTo">'2008-04-19' AND o.vendor=v.nr ORDER BY o.price LIMIT 10;
