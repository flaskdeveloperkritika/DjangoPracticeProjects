# Generated by Django 4.0.2 on 2022-05-06 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Familymembers', '0002_familymember_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='familymember',
            name='pay_slip',
            field=models.FileField(default=None, null=True, upload_to='static/payslips'),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='profile_image',
            field=models.FileField(default=None, null=True, upload_to='static/profileimages'),
        ),
    ]