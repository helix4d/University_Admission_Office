from django.contrib import admin
from applicant_db.models import *


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    pass


@admin.register(EducationForm)
class EducationFormAdmin(admin.ModelAdmin):
    pass


@admin.register(LevelOfStudy)
class LevelOfStudyAdmin(admin.ModelAdmin):
    pass

