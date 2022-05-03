from django.db import models


class FamilyMember(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=14)
    work = models.CharField(max_length=50)
    income = models.FloatField()
    profile_image = models.FileField(upload_to='static/profileimages', default=None, null=True)
    pay_slip = models.FileField(upload_to='static/payslips', default=None, null=True)

    def __str__(self):
        return self.name