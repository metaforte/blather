from django.db import models

from django.db.models import (CharField, TextField, DateField, SlugField, DateTimeField, URLField, ForeignKey)
# Create your models here.

class Blat (models.Model):
    text = TextField()
    created_on = DateTimeField (auto_now_add=True)
    via = URLField(blank=True)

    def total_likes(self):
        return self.like_set.count()

    def __str__ (self):
        return self.text

class Like (models.Model):
    blat = ForeignKey (Blat)