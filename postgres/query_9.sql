SELECT p.nr, p.name, p.mbox_sha1sum, p.country, r2.nr, r2.product, r2.title FROM review r, person p, review r2 WHERE r.nr=4 AND r.person=p.nr AND r2.person=p.nr LIMIT 10;
