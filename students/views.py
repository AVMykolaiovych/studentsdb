from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def students_list(request):
    students = (
        {'id': 1,
         'first_name': 'Віталій',
         'last_name': 'Подоба',
         'ticket': 235,
         'image': 'img/1.jpg'},
        {'id': 2,
         'first_name': 'Андрій',
         'last_name': 'Корост',
         'ticket': 2123,
         'image': 'img/2.jpg'},
        {'id': 3,
         'first_name': 'Богдан',
         'last_name': 'Бондарчук',
         'ticket': 2345,
         'image': 'img/3.jpg'},
    )
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
         'group_head': 'Ячменеев Олег'},
        {'id': 2,
         'group_name': 'МтМ-22',
         'group_head': 'Подоба Віталій'},
        {'id': 3,
         'group_name': 'МтМ-23',
         'group_head': 'Бондарчук Богдан'},
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


