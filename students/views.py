from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.


def students_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students/students_list.html', context)


def students_add(request):
    return HttpResponse('<h1>Students add form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit students %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete students %s</h1>' % sid)


def groups_list(request):
    groups = (
        {'id': 1,
         'group_name': 'МтМ-21',
         'group_head': {'id': 1, 'name': 'Ячменеев Олег'}},
        {'id': 2,
         'group_name': 'МтМ-22',
         'group_head': {'id': 2, 'name': 'Подоба Віталій'}},
        {'id': 3,
         'group_name': 'МтМ-23',
         'group_head': {'id': 3, 'name': 'Бондарчук Богдан'}},
    )
    context = {
        'groups': groups
    }
    return render(request, 'students/groups_list.html', context)


def groups_add(request):
    return HttpResponse('<h1>Groups add form</h1>')


def groups_edit(request, sid):
    return HttpResponse('<h1>Edit groups %s</h1>' % sid)


def groups_delete(request, sid):
    return HttpResponse('<h1>Delete groups %s</h1>' % sid)


def journal_list(request):
    return render(request, 'students/journal_list.html')


