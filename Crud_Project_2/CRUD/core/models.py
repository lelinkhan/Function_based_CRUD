from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=100, default="")
    student_id = models.IntegerField()
