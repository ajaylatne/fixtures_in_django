from django.db import models

# python manage.py loaddata student_data.json


class Student(models.Model):
    name = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
