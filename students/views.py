from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def students_list(request):
    return render(request, 'students/students_list.html', {})


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