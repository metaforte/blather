
All commands

Init the repo. Create project, start the first app
```

(django182) c:\pyprojects\>

mkdir blather
cd blather
git init .

git remote add origin https://github.com/pikeview/blather.git

git push -u origin master

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


Request response cycle
----------------------

Server creates dispatcher object from url mappings 
Browser -> Request -> Server -> Convert request into request python object -> dispatcher uses url route mappings and routes the request -> Middleware-> Views & Mixins -> View interacts with Templates and Forms and Mixins -> ORM -> SQL 

DB

References
----------
https://gitlab.com/jeremytiki/MasterDjangoWebDev


Implementing `__str__` method in Python 2
-----------------------------------------
```Python
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
@python_2_unicode_compatible
Class Amodel (models.Model):
    def __str__(self):
        pass
```