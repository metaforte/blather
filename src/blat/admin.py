from django.contrib import admin

# Register your models here.
from .models import Blat

class BlatAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_on', 'total_likes')
    list_filter = ['created_on']
    search_fields = ['text']
    
admin.site.register(Blat, BlatAdmin)