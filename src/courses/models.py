from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible
class Course(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return  "id={0} ,name= {1}".format(self.id ,self.name)

'''
   access db using sqlite3 db.sqlite3
   sqlite> .tables
   table names will  have appname_tablename format (courses_course)
   sqlite> schema coures_course
'''