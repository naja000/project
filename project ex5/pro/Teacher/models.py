from django.db import models

# Create your models here.
class StudentModel(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.CharField(max_length=300)
    phone=models.IntegerField()
    email=models.EmailField()
    image=models.ImageField(upload_to="student_images",null=True)
    


