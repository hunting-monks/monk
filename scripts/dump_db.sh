#!/usr/bin/bash
for tbl in $(mysql -s -e "show tables from monk" -u monk --password="monk" | grep -v Tables_in)
do
  echo "Dumping $tbl..."
  mysqldump -u monk monk $tbl  --password="monk"> sql/$tbl.dat
done
