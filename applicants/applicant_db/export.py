import requests
import xlsxwriter
from django.urls import resolve
from django.contrib.auth.decorators import login_required
import applicant_db.app_logger as app_logger
from applicant_db.models import *
from applicant_db.statistic import *
import os
import datetime


def export_to_excele():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    offset = datetime.timezone(datetime.timedelta(hours=3))
    filename = 'lists' + datetime.datetime.now(offset).strftime("%d-%m-%y_%H:%M")
    filepath = BASE_DIR + '/files/' + filename + '.xlsx'

    workbook = xlsxwriter.Workbook(filepath)
    applicants = Applicant.objects.all()
    students = Student.objects.all()
    worksheet_applicants = workbook.add_worksheet('Абитуриенты ХТУ')
    worksheet_students = workbook.add_worksheet('Студенты ХТУ')
    applicants_list = []
    for applicant in applicants:
        if applicant.hostel == True:
            hostel = 'Нужно'
        else:
            hostel = 'Ненужно'
        applicant_fields = [
            applicant.last_name,
            applicant.first_name,
            applicant.middle_name,
            applicant.phone,
            applicant.email,
            applicant.address,
            applicant.education_doc,
            applicant.passport,
            applicant.ic,
            hostel,
            applicant.benefits,
            str(applicant.education_form),
            str(applicant.specialization)
        ]
        applicants_list.append(applicant_fields)

        header = workbook.add_format({'fg_color': '#ffffff', 'color': '#000000'})
        worksheet_applicants.write('A1', 'Фамилия', header)
        worksheet_applicants.write('B1', 'Имя', header)
        worksheet_applicants.write('C1', 'Отчество', header)
        worksheet_applicants.write('D1', 'Телефон', header)
        worksheet_applicants.write('E1', 'email', header)
        worksheet_applicants.write('F1', 'Адрес', header)
        worksheet_applicants.write('G1', 'Документ об образовании', header)
        worksheet_applicants.write('H1', 'Номер паспорта', header)
        worksheet_applicants.write('I1', 'Идентификационный код', header)
        worksheet_applicants.write('J1', 'Общежитие', header)
        worksheet_applicants.write('K1', 'Льготы', header)
        worksheet_applicants.write('L1', 'Форма обучения', header)
        worksheet_applicants.write('M1', 'Специальность', header)
        row_num = 1
        for row_data in applicants_list:
            worksheet_applicants.write_row(row_num, 0, row_data)
            row_num += 1
    students_list = []
    for student in students:
        if student.hostel:
            hostel = 'Нужно'
        else:
            hostel = 'Ненужно'
        student_fields = [
            student.last_name,
            student.first_name,
            student.middle_name,
            student.phone,
            student.email,
            hostel,
            student.benefits,
            student.curs,
            student.group,
            student.prog,
            student.level,
            str(student.education_form),
            str(student.specialization)
        ]
        students_list.append(student_fields)

        header = workbook.add_format({'fg_color': '#ffffff', 'color': '#000000'})
        worksheet_students.write('A1', 'Фамилия', header)
        worksheet_students.write('B1', 'Имя', header)
        worksheet_students.write('C1', 'Отчество', header)
        worksheet_students.write('D1', 'Телефон', header)
        worksheet_students.write('E1', 'email', header)
        worksheet_students.write('F1', 'Общежитие', header)
        worksheet_students.write('G1', 'Льготы', header)
        worksheet_students.write('H1', 'Курс', header)
        worksheet_students.write('I1', 'Группа', header)
        worksheet_students.write('J1', 'Образовательная программа', header)
        worksheet_students.write('K1', 'Уровень обучения', header)
        worksheet_students.write('L1', 'Форма обучения', header)
        worksheet_students.write('M1', 'Специальность', header)
        row_num = 1
        for row_data in students_list:
            worksheet_students.write_row(row_num, 0, row_data)
            row_num += 1

    workbook.close()


def get_by_education_forms():
    education_forms_applicants = {}
    education_forms_students = {}
    forms = EducationForm.objects.all()
    for form in forms:
        education_forms_applicants[form.name] = Applicant.objects.filter(education_form=form)
        education_forms_students[form.name] = Student.objects.filter(education_form=form)
    return education_forms_applicants, education_forms_students


def get_by_specializations():
    specializations_applicants = {}
    specializations_students = {}
    specialization = Specialization.objects.all()
    for specialization in specializations_applicants:
        specializations_applicants[specialization.name] = Applicant.objects.filter(specialization=specialization)
    for specialization in specializations_students:
        specializations_students[specialization.name] = Student.objects.filter(specialization=specialization)
    return specializations_applicants, specializations_students
