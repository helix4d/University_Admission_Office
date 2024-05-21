import operator

from applicant_db.models import *
from datetime import datetime
from django.db.models import Count


def get_statistic():
    applicants = Applicant.objects.count()
    students = Student.objects.count()
    all = applicants + students
    stat = {
        'all': all,
        'applicants': applicants,
        'students': students,
        'forms': get_education_forms(),
        'specialisation': get_specialisation(),
        'hostel_applicants': Applicant.objects.filter(hostel=1).count(),
        'hostel_students': Student.objects.filter(hostel=1).count()
    }
    return stat


def get_education_forms():
    education_forms = {}
    forms = EducationForm.objects.all()
    for form in forms:
        education_forms[form.name] = {
            'applicant': Applicant.objects.filter(education_form=form).count(),
            'student': Student.objects.filter(education_form=form).count()
        }
    return education_forms


def get_specialisation():
    specialisations = {}
    specs = Specialization.objects.all()
    for spec in specs:
        id = spec.id
        specialisations[spec.name] = {
            'applicant': Applicant.objects.filter(specialization_id=id).count(),
            'student': Student.objects.filter(specialization_id=id).count()
        }
    return specialisations


def get_work_dates():
    applicants = Applicant.objects.all().values('created')
    applicants_dates = set()
    for date in applicants:
        d = date['created'].date()
        applicants_dates.add(d)

    students = Student.objects.all().values('created')
    students_dates = set()
    for date in students:
        d = date['created'].date()
        students_dates.add(d)

    dates_set = applicants_dates | students_dates
    dates_list = list(dates_set)

    sorted_dates = sorted(dates_list)
    return sorted_dates


def day_stat_specialisation(date):
    specialisations = {}
    specs = Specialization.objects.all()
    for spec in specs:
        id = spec.id
        specialisations[spec.name] = {
            'applicant': Applicant.objects.filter(created__date=date, specialization_id=id).count(),
            'student': Student.objects.filter(created__date=date, specialization_id=id).count()
        }
    return specialisations


def day_stat(dates):
    day_stat = {}
    for date in dates:
        applicants = Applicant.objects.all().filter(created__date=date).order_by('created__date').count()
        students = Student.objects.all().filter(created__date=date).order_by('created__date').count()
        specialisations = day_stat_specialisation(date)
        day_stat[str(date)] = {
            'applicants': applicants,
            'students': students,
            'specialisations': specialisations
        }
    return day_stat


def days_stat(dates):
    day_stat = {}
    for date in dates:
        applicants = Applicant.objects.all().filter(created__date=date).order_by('created__date').count()
        students = Student.objects.all().filter(created__date=date).order_by('created__date').count()
        specialisations = day_stat_specialisation(date)
        all = applicants + students
        day_stat[str(date)] = {
            'all': all,
            'applicants': applicants,
            'students': students,
            'specialisations': specialisations
        }
        print(day_stat)
    return day_stat
