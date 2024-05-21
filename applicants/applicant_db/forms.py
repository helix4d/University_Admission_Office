from django import forms
from django.forms import ModelForm
from applicant_db.models import *


class ApplicantForm(ModelForm):

    class Meta:
        model = Applicant
        fields = (
            'last_name',
            'first_name',
            'middle_name',
            'phone',
            'email',
            'address',
            'education_doc',
            'passport',
            'ic',
            'hostel',
            'benefits',
            'education_form',
            'specialization',
            'level_of_study'
        )


class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = (
            'last_name',
            'first_name',
            'middle_name',
            'phone',
            'email',
            'curs',
            'group',
            'prog',
            'level',
            'education_form',
            'specialization',
            'level_of_study'
        )

