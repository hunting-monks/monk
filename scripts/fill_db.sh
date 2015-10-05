#!/bin/sh
for i in `ls sql`
do
    mysql -u monk --password="monk" monk < sql/$i
done
