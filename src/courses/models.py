from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200)

'''
   access db using sqlite3 db.sqlite3
   sqlite> .tables
   table names will  have appname_tablename format (courses_course)
   sqlite> schema coures_course
'''