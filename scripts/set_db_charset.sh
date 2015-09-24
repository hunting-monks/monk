#!/bin/bash
DB="monk"
(
    echo 'ALTER DATABASE `'"$DB"'` CHARACTER SET utf8 COLLATE utf8_general_ci;'
    mysql -u monk --password="monk" "$DB" -e "SHOW TABLES" --batch --skip-column-names \
    | xargs -I{} echo 'ALTER TABLE `'{}'` CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;'
) \
| mysql -u monk --password="monk" $DB