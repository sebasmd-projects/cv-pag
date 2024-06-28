# Generated by Django 4.2.7 on 2024-06-28 00:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_usermodel_options_alter_usermodel_country_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='default_order',
            field=models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='priority'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is active'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='language',
            field=models.CharField(blank=True, default='es', max_length=50, null=True, verbose_name='language'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='updated'),
        ),
    ]
