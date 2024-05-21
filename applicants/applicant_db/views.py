from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from applicant_db.forms import *
from applicant_db.models import *
import datetime
import os
from django.core.exceptions import ObjectDoesNotExist
from django.urls import resolve
from django.contrib.auth.decorators import login_required
import applicant_db.app_logger as app_logger
import applicant_db.statistic as stat
import applicant_db.export as export


def index(request):
    applicants = Applicant.objects.count()
    students = Student.objects.count()
    contingent = applicants + students
    data = {
        'title': 'Главная ХГМА',
        'applicants': applicants,
        'students': students,
        'contingent': contingent
        }

    return render(request, 'index.html', context=data)


def stat_all(request):
    data = stat.get_statistic()
    return render(request, 'stat_all.html', context=data)


def stat_days(request):
    dates = stat.get_work_dates()
    data = stat.day_stat(dates)
    print(data)
    return render(request, 'stat_days.html', {'data': data})


def stat_index(request):
    data = stat.get_statistic()
    return render(request, 'stat_index.html', context=data)


def applicants(request):
    applicants = Applicant.objects.all()
    count = applicants.count()
    data = {'applicants': applicants, 'title': 'Академия', 'count': count}
    return render(request, 'applicants.html', context=data)


def applicant_create(request):
    form = {'form': ApplicantForm()}
    return render(request, 'applicant_create.html', context=form)


def applicant_save(request):
    if request.method == "POST":
        applicant_form_data = ApplicantForm(request.POST)
        applicant = applicant_form_data.save()
        app_logger.log_new(request, applicant.pk)
    return HttpResponseRedirect(reverse('applicants'))


def applicant_edit(request, id):
    applicant = Applicant.objects.get(pk=id)
    form = {'form': ApplicantForm(instance=applicant), 'id': id}
    return render(request, 'applicant_edit.html', context=form)


def applicant_edit_save(request, id):
    if request.method == "POST":
        applicant = Applicant.objects.get(pk=id)
        form = ApplicantForm(request.POST, instance=applicant)
        if form.is_valid():
            applicant_edited = form.save()
            app_logger.log_edit(request, applicant_edited.pk)
            return HttpResponseRedirect(reverse('applicants'))
        else:
            return render(request, 'applicant_edit.html', context=form)


def applicant(request, id):
    applicant = get_object_or_404(Applicant, pk=id)
    class_name = applicant.get_class_name()
    return render(request, 'applicant.html', {'applicant': applicant, 'class_name': class_name})


def applicant_delete(request, id):
    applicant = Applicant.objects.get(pk=id)
    try:
        applicant.delete()
        app_logger.log_delete(request, id)
        return HttpResponseRedirect(reverse("applicants"))
    except ObjectDoesNotExist:
        return HttpResponseNotFound("<h2>Абитурьент не найден</h2>")


def profile(request):
    return redirect('/')


def exports(request):
    export.export_to_excele()
    return redirect('download')


@login_required(login_url='/accounts/login/')
def applicants_download(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = BASE_DIR + '/files/'
    list_of_files = os.listdir(path)
    app_logger.log_export(request)
    return render(request, 'download.html', {'list_of_files': list_of_files})


def students(request):
    students = Student.objects.all()
    count = students.count()
    data = {'students': students, 'title': 'Академия', 'count': count}
    return render(request, 'students.html', context=data)


def student_create(request):
    form = {'form': StudentForm()}
    return render(request, 'student_create.html', context=form)


def student_save(request):
    if request.method == "POST":
        student_form_data = StudentForm(request.POST)
        student = student_form_data.save()
        app_logger.log_new(request, student.pk)
    return HttpResponseRedirect(reverse('students'))


def student_edit(request, id):
    student = Student.objects.get(pk=id)
    form = {'form': StudentForm(instance=student), 'id': id}
    return render(request, 'student_edit.html', context=form)


def student_edit_save(request, id):
    if request.method == "POST":
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student_edited = form.save()
            app_logger.log_edit(request, student_edited.pk)
            return HttpResponseRedirect(reverse('students'))
        else:
            return render(request, 'student_edit.html', context=form)


def student(request, id):
    student = get_object_or_404(Student, pk=id)
    class_name = student.get_class_name()
    return render(request, 'student.html', {'student': student, 'class_name': class_name})


def student_delete(request, id):
    student = Student.objects.get(pk=id)
    try:
        student.delete()
        app_logger.log_delete(request, id)
        return HttpResponseRedirect(reverse("students"))
    except ObjectDoesNotExist:
        return HttpResponseNotFound("<h2>Студент не найден</h2>")


def list_applicants_by_specialisations(request):
    applicants = {}
    specializations = Specialization.objects.all()
    for specialization in specializations:
        id = specialization.id
        applicants[specialization.name] = {
            'applicants': Applicant.objects.filter(specialization_id=id)
        }
    return render(request, 'applicants_by_specialisation.html', {'applicants': applicants})


def list_students_by_specialisations(request):
    students = {}
    specializations = Specialization.objects.all()
    for specialization in specializations:
        id = specialization.id
        students[specialization.name] = {
            'students': Student.objects.filter(specialization_id=id)
        }
    return render(request, 'students_by_specialisation.html', {'students': students})
