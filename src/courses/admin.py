from django.contrib import admin

class CourseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Course,CourseAdmin)
