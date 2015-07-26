# monk
hunting HR V1

# Prerequsites

Run script/install_unbuntu.sh to install all packages needed.

Run "pip install -r scripts/pymodules" to install python packages

# Quick Start
1. Create a virtualenv dir

	virtualenv monkproject

	cd monkproject

	source ./bin/activate

2. Create database 'monk' in mysql

3. Create django tables

	python manage.py migrate

4. Bringup webserver

	python manage.py runserver

	access http://127.0.0.1:8000

## Create models
1. (Skip this if you are not adding a new model), otherwise run the following.

	python manage.py makemigrations myapp

2. Check sql that creates tables

	python manage.py sqlmigrate myapp 0001

3. Create tables

	python manage.py migrate

# Django
## Check Django version

	python -c "import django; print(django.get_version())"

## Create admin superuser

	python manage.py createsuperuser


# MySQL
## Create DB and user
mysql -u root -p

	CREATE DATABASE monk;

	CREATE USER 'monk'@'localhost';

	GRANT ALL ON monk.* TO 'monk'@'localhost';

