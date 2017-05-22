# _*_ coding: utf-8 _*_

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Віталій',
         'last_name': u'Подоба',
         'ticket': 235,
         'image': 'img/1.jpg'},
        {'id': 2,
         'first_name': u'Андрій',
         'last_name': u'Корост',
         'ticket': 2123,
         'image': 'img/2.jpg'},
        {'id': 3,
         'first_name': u'Богдан',
         'last_name': u'Бондарчук',
         'ticket': 2345,
         'image': 'img/3.jpg'},
    )
    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):
    return HttpResponse('<h1>Students add form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit students %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete students %s</h1>' % sid)


def groups_list(request):
    return HttpResponse('<h1>Groups listing</h1>')


def groups_add(request):
    return HttpResponse('<h1>Groups add form</h1>')


def groups_edit(request, sid):
    return HttpResponse('<h1>Edit groups %s</h1>' % sid)


def groups_delete(request, sid):
    return HttpResponse('<h1>Delete groups %s</h1>' % sid)