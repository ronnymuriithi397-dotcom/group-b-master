import datetime

from django.db import models

# Create your models here.
class Student(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='student/', null=True, blank=True)
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(default='gender')
    date = models.CharField(default=datetime.date.today)

    def __str__(self):
        return self.name
class Exam(models.Model):
    name = models.CharField(max_length=50)
    exam_code = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name