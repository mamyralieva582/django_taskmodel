from django.db import models

# Create your models here.
class Student(models.Model):
    first_name  = models.CharField(max_length=40, verbose_name='Имя')
    
    last_name = models.CharField(max_length=40, verbose_name='Фамилия')
    
    email = models.EmailField

    age = models.IntegerField(verbose_name='Возраст') 

    uptated_at = models.DateTimeField(auto_now=True)

    created_at = models.DateTimeField(auto_now_add=True)


class Course(models.Model):
    name = models.CharField(max_length= 100, verbose_name = 'Имя')
    description = models.TextField(max_length=500, blank=True, verbose_name = 'Описание')
    student = models.ManyToManyField(Student, related_name='student', verbose_name='Студент')