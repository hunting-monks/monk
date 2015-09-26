# monk hunting HR V1

Prerequsites
=================
Run the following to install all packages needed.

```
script/install_unbuntu.sh
pip install -r scripts/pymodules
```

Quick Start
=================
0, install basic applications (for mac only)
```
	brew install mysql
	brew install node
	ln -sfv /usr/local/opt/mysql/*.plist ~/Library/LaunchAgents
	ln -sfv /usr/local/opt/node/*.plist ~/Library/LaunchAgents
```
Note Pillow is needed to handle django ImageField.
In order to install Pillow on OS X later than 10.8, run the following,
```
	xcode-select --install
```

1, Create a virtualenv dir
```
	virtualenv monkproject
	cd monkproject
	source ./bin/activate
```

2, Create database 'monk' in mysql
```
mysql -u root -p

	>CREATE DATABASE monk CHARACTER SET utf8;;
	>CREATE USER 'monk'@'localhost' IDENTIFIED BY 'monk';
	>GRANT ALL PRIVILEGES ON * . * TO 'monk'@'localhost'; FLUSH PRIVILEGES;
```

3, Create django tables
```
	python manage.py migrate
```

4, Fill in test data to DB
```
	cd scripts
	. fill_db.sh
```

5, Generate Chinese translation file
```
   	export DJANGO_SETTINGS_MODULE=monksite.settings
   	django-admin compilemessages
```

6, Bringup webserver, then access http://127.0.0.1:8000
```
	python manage.py runserver
```

7, Login with test account. Three accounts have been created in the dev data.
```
	username: admin    password: admin
        username: monk     password: monk    -- this is a recruiter account
	username: interviewer password: monk -- this is an interviewer account
```

Misc Notes
===================
Create models
---------------------
1, (Skip this if you are changing any model), otherwise run the following.
```
	python manage.py makemigrations myapp
```
2, Check sql that creates tables
```
	python manage.py sqlmigrate myapp 0001
```
3, Create tables
```
	python manage.py migrate
```

Check Django version
-----------------------
```
	python -c "import django; print(django.get_version())"
```

Create admin superuser
-----------------------
```
	python manage.py createsuperuser
```
