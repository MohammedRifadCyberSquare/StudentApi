from django.db import models

# Create your models here.


class Student(models.Model):
    student_name = models.CharField(max_length=500)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    student_pic = models.ImageField(upload_to = 'student/')


    class Meta:
        db_table = 'student'