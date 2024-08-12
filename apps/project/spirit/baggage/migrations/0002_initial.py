# Generated by Django 4.2.7 on 2024-07-28 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('baggage', '0001_initial'),
        ('spirit_core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='baggageshippingmodel',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='baggageshipping_user', to=settings.AUTH_USER_MODEL, verbose_name='Agent'),
        ),
        migrations.AddField(
            model_name='baggageshippingmodel',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gaggageshipping_flight', to='spirit_core.flightmodel', verbose_name='Flight'),
        ),
    ]