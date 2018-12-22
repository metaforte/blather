
All commands

Init the repo. Create project, start the first app
```

(django182) c:\pyprojects\>

mkdir blather
cd blather
git init .

django-admin startproject config

mv config src

cd src

python manage.py startapp blat

```
Add the new app to  config/settings.py in INSTALLED_APPS section

```
python manage.py runserver

python manage.py migrate

python manage.py createsuperuser #admin, admin

```

edit blat/admin.py and add BlatAdmin class details

```
python manage.py makemigrations

python manage.py emigrate
```