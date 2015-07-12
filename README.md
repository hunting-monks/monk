# monk
hunting HR V1

# Prerequsites
Run script/install_unbuntu.sh to install all packages needed.

# Django
## Check Django version
python -c "import django; print(django.get_version())"

# MySQL
## Create DB and user
mysql -u root -p
> CREATE DATABASE monk;
> CREATE USER 'monk'@'localhost';
> GRANT ALL ON monk.* TO 'monk'@'localhost';

