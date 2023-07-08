from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'

    students_object_list = Student.objects.all().prefetch_related('teachers')
    teacher_object_list = Teacher.objects.all()

    # print(students_object_list)
    # print(teacher_object_list)
    #
    # for student in students_object_list:
    #     print(student.name, '-', student.teachers.all())
    #     if not student.teachers.all():
    #         student.teachers.add(teacher_object_list.get(id=student.teacher))

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    context = {
        'object_list': students_object_list.order_by(ordering)
    }

    return render(request, template, context)
