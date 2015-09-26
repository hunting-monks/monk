#!/bin/sh
for i in `ls sql`
do
    echo "mysql -u monk monk --password=\"monk\" < $i"
done
#    mysql -u monk monk --password="monk" < $i