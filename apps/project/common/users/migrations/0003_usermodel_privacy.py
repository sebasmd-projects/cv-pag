# Generated by Django 4.2.7 on 2024-07-17 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usermodel_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='privacy',
            field=models.BooleanField(default=False, verbose_name='terms and conditions'),
        ),
    ]