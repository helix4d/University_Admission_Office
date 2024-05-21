from django.db import models
from django.contrib.auth.models import User


class Applicant(models.Model):
    objects = models.Manager()
    last_name = models.CharField(max_length=24, verbose_name='Фамилия')
    first_name = models.CharField(max_length=16, verbose_name='Имя')
    middle_name = models.CharField(max_length=16, verbose_name='Отчество')
    phone = models.CharField(max_length=16, verbose_name='Телефон', blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=256, verbose_name='Адрес')
    education_doc = models.CharField(max_length=256, verbose_name='Документ об образовании', blank=True)
    passport = models.CharField(max_length=512, verbose_name='Номер паспорта', blank=True)
    ic = models.CharField(max_length=64, verbose_name='Идентификационный код', blank=True)
    hostel = models.BooleanField(default=False, verbose_name='Необходимость в общежитии', blank=True)
    benefits = models.CharField(max_length=256, verbose_name='Льготы', blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')
    changed = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    list_display = ('first_name', 'middle_name', 'last_name')
    education_form = models.ForeignKey(
        'EducationForm',
        on_delete=models.PROTECT,
        verbose_name='Форма обучения',
        blank=True)
    specialization = models.ForeignKey(
        'Specialization',
        on_delete=models.PROTECT,
        verbose_name='Специальность',
        blank=True)
    level_of_study = models.ForeignKey(
        'LevelOfStudy',
        on_delete=models.PROTECT,
        verbose_name='Уровень обучения',
        blank=True)


    def __str__(self):
        id = str(self.pk)
        last_name = str(self.last_name)
        first_name = str(self.first_name)
        middle_name = str(self.middle_name)
        name = id + '. ' + last_name + ' ' + first_name + ' ' + middle_name
        return name

    def get_class_name(self):
        return self.__class__.__name__

    class Meta:
        verbose_name_plural = 'Абитуриенты ХТУ'
        verbose_name = 'Абитуриент ХТУ'
        ordering = ['-created']


class Specialization(models.Model):
    name = models.CharField(max_length=256, verbose_name='Специальность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Специальности ХТУ'
        verbose_name = 'Специальность ХТУ'


class EducationForm(models.Model):
    name = models.CharField(max_length=24, verbose_name='Форма обучения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Формы обучения в ХТУ'
        verbose_name = 'Форма обучения в ХТУ'


class LevelOfStudy(models.Model):
    name = models.CharField(max_length=24, verbose_name='Уровень обучения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Уровни обучения в ХТУ'
        verbose_name = 'Уровень обучения в ХТУ'


class Student(models.Model):
    objects = models.Manager()
    last_name = models.CharField(max_length=24, verbose_name='Фамилия')
    first_name = models.CharField(max_length=16, verbose_name='Имя')
    middle_name = models.CharField(max_length=16, verbose_name='Отчество')
    phone = models.CharField(max_length=16, verbose_name='Телефон', blank=True)
    email = models.EmailField(verbose_name='Электронная почта', blank=True)
    hostel = models.BooleanField(default=False, verbose_name='Необходимость в общежитии', blank=True)
    benefits = models.CharField(max_length=256, verbose_name='Льготы', blank=True)
    curs = models.IntegerField(verbose_name='Курс', blank=True, null=True)
    group = models.CharField(max_length=16, verbose_name='Группа', blank=True)
    prog = models.CharField(max_length=512, verbose_name='Образовательная программа', blank=True)
    level = models.CharField(max_length=256, verbose_name='Уровень обучения', blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')
    changed = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    education_form = models.ForeignKey(
        'EducationForm',
        on_delete=models.PROTECT,
        verbose_name='Форма обучения',
        blank=True)
    specialization = models.ForeignKey(
        'Specialization',
        on_delete=models.PROTECT,
        verbose_name='Специальность',
        blank=True)
    level_of_study = models.ForeignKey(
        'LevelOfStudy',
        on_delete=models.PROTECT,
        verbose_name='Уровень обучения',
        blank=True)
    list_display = ('first_name', 'middle_name', 'last_name')

    def __str__(self):
        id = str(self.pk)
        last_name = str(self.last_name)
        first_name = str(self.first_name)
        middle_name = str(self.middle_name)
        name = id + '. ' + last_name + ' ' + first_name + ' ' + middle_name
        return name

    def get_class_name(self):
        return self.__class__.__name__

    class Meta:
        verbose_name_plural = 'Студенты ХТУ'
        verbose_name = 'Студент ХТУ'
        ordering = ['-created']
