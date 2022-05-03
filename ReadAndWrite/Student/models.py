from django.db import models


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_branch = models.CharField(max_length=100)
    student_univ = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name

