# monk
hunting HR V1

# Prerequsites

Run script/install_unbuntu.sh to install all packages needed.

Run "pip install -r scripts/pymodules" to install python packages

# Quick Start
0. install basic applications
	brew install mysql

	brew install node

	ln -sfv /usr/local/opt/mysql/*.plist ~/Library/LaunchAgents

	ln -sfv /usr/local/opt/node/*.plist ~/Library/LaunchAgents

1. Create a virtualenv dir

	virtualenv monkproject

	cd monkproject

	source ./bin/activate

2. Create database 'monk' in mysql

3. Create django tables

	python manage.py migrate

4. Generate Chinese translation file

   	export DJANGO_SETTINGS_MODULE=monksite.settings
   	django-admin compilemessages

5. Bringup webserver

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

	CREATE USER 'monk'@'localhost' IDENTIFIED BY 'monk';

	GRANT ALL PRIVILEGES ON * . * TO 'monk'@'localhost'; FLUSH PRIVILEGES;


