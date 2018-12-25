from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#test using http://127.0.0.1:8000 or http://127.0.0.1:8000/

def my_first_view_v1(request):
    return HttpResponse ("Hello World")

#test using http://127.0.0.1:8000/Manas/
#url(r'^(?P<who>.*)/$', my_first_view),
#This also matches http://127.0.0.1:8000/Manas/test/test2 
def my_first_view_v2(request, who):
    return HttpResponse ("Hello %s !" % who)

#start using templates
def my_first_view_v3(request, who):
    return render (request, 'courses/hello.html',context={'who':who,})

from .models import Course
from django.shortcuts import get_object_or_404
def course_detail(request, course_id):
    course = get_object_or_404 (Course,id=course_id)
    return render(request, 'courses/course_detail.html', {'course':course})
