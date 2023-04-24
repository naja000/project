from django.db import models

# Create your models here.
class TeacherModel(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.EmailField()
    Qualification=models.CharField(max_length=100)
