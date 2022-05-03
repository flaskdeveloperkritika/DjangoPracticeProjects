from django.db import models


class Trainee(models.Model):
    trainee_name = models.CharField(max_length=100)
    reg_id = models.IntegerField()
    phone_number = models.BigIntegerField()
    subject = models.CharField(max_length=50)

