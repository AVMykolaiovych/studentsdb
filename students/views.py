from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Student, Group

# Create your views here.


def students_list(request):
    students = Student.objects.all()

    order_by = request.GET.get('order_by', '')
    if order_by in ('first_name', 'last_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):
    return HttpResponse('<h1>Students add form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit students %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete students %s</h1>' % sid)


def groups_list(request):
    groups = Group.objects.all()

    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'leader'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()

    paginator = Paginator(groups, 3)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        groups = paginator.page(1)
    except EmptyPage:
        groups = paginator.page(paginator.num_pages)

    return render(request, 'students/groups_list.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Groups add form</h1>')


def groups_edit(request, sid):
    return HttpResponse('<h1>Edit groups %s</h1>' % sid)


def groups_delete(request, sid):
    return HttpResponse('<h1>Delete groups %s</h1>' % sid)


def journal_list(request):
    return render(request, 'students/journal_list.html')


