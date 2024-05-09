from django.db import models

class Books(models.Model):

    title = models.CharField(max_length=40, verbose_name='Название',default=None)
    
    description = models.TextField(blank=True, verbose_name='Описание')

    owner = models.CharField(unique=True, max_length=20,verbose_name='владелец')


    def __str__(self):
        return self.title 
    








