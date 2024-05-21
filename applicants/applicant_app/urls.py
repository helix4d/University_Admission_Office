from django.contrib import admin
from django.urls import path, include
from applicant_db import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('exports/', views.exports, name='exports'),
    path('download/', views.applicants_download, name='download'),
    path('applicants/', views.applicants, name='applicants'),
    path('applicant/create', views.applicant_create, name='applicant_create'),
    path('applicant/save/', views.applicant_save, name='applicant_save'),
    path('applicant/edit/<int:id>/', views.applicant_edit, name='applicant_edit'),
    path('applicant/edit/save/<int:id>/', views.applicant_edit_save, name='applicant_edit_save'),
    path('applicant/<int:id>/', views.applicant, name='applicant'),
    path('applicant/delete/<int:id>/', views.applicant_delete, name='applicant_delete'),
    path('students/', views.students, name='students'),
    path('student/create/', views.student_create, name='student_create'),
    path('student/save/', views.student_save, name='student_save'),
    path('student/edit/<int:id>/', views.student_edit, name='student_edit'),
    path('student/edit/save/<int:id>/', views.student_edit_save, name='student_edit_save'),
    path('student/<int:id>/', views.student, name='student'),
    path('student/academy/delete/<int:id>/', views.student_delete, name='student_delete'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('accounts/profile/', views.profile, name='user_profile'),
    path('statistic/', views.stat_all, name='stat-index'),
    path('statistic/days', views.stat_days, name='stat-days'),
    path('applicants/byspecialisations/', views.list_applicants_by_specialisations, name='applicants_list_by_specialisations'),
    path('students/byspecialisations/', views.list_students_by_specialisations, name='students_list_by_specialisations')
]
urlpatterns += static(settings.FILES_URL, document_root=settings.FILES_ROOT)