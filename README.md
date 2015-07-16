# monk
hunting HR V1

# Prerequsites

Run script/install_unbuntu.sh to install all packages needed.

Run "pip install -r scripts/pymodules" to install python packages
  
# Django

## Check Django version
python -c "import django; print(django.get_version())"

## Create django tables in database
* Create database 'monk' in mysql
* Run "python manage.py migrate"

# MySQL
## Create DB and user
mysql -u root -p
 > CREATE DATABASE monk;
 > CREATE USER 'monk'@'localhost';
 > GRANT ALL ON monk.* TO 'monk'@'localhost';

