from django.db import models

# python manage.py loaddata student_data.json  --> to pass data from fixture file to db

# py manage.py dumpdata app1.Student --output=app1/fixtures/student_data.json --> to fetch data from db and add into fixture file


class Student(models.Model):
    name = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
