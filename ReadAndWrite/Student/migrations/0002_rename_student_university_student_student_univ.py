# Generated by Django 4.0.2 on 2022-05-02 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_university',
            new_name='student_univ',
        ),
    ]