from django.contrib.auth.models import User
from django.db import models
from django.db.models import DateTimeField


# Create your models here.


class Task(models.Model):
    statuses = [('pendiente', 'Pendiente'),
                ('progreso', 'Progreso'),
                ('hecho', 'Hecho')]
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    created_at = DateTimeField('Creado', auto_now_add=True, db_index=True)
    updated_at = DateTimeField('Actualizado', auto_now=True)
    status = models.CharField(choices=statuses, max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
