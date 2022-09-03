from django.db import models

# Create your models here.

class AddStudent(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    date_of_birth = models.DateField(auto_now_add=False , max_length=12)
    grade = models.IntegerField()
    


