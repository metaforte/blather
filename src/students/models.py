
from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# ===========  Recreate User tables ===============
#del db.sqlite3
#python manage.py makemigrations
#python manage.py migrate
#python manage.py createsuperuser