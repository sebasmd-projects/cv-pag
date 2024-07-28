# Generated by Django 4.2.7 on 2024-07-28 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('baggage', '0002_initial'),
        ('rampone', '0001_initial'),
        ('spirit_core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useractivitychecklistmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='useractivitychecklist_user', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='rampdatamodel',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rampdata_user', to=settings.AUTH_USER_MODEL, verbose_name='Agent'),
        ),
        migrations.AddField(
            model_name='rampdatamodel',
            name='baggage_shipping',
            field=models.ManyToManyField(related_name='rampdata_baggageshipping', to='baggage.baggageshippingmodel', verbose_name='baggage shipping'),
        ),
        migrations.AddField(
            model_name='rampdatamodel',
            name='flight_arrival',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='flight_arrival', to='spirit_core.flightmodel', verbose_name='Flight arrival'),
        ),
        migrations.AddField(
            model_name='rampdatamodel',
            name='flight_departure',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='flight_departure', to='spirit_core.flightmodel', verbose_name='Flight departure'),
        ),
        migrations.AddField(
            model_name='activitytimeentrymodel',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activitytimeentry_activity', to='rampone.activitynameschecklistmodel', verbose_name='activity'),
        ),
        migrations.AddField(
            model_name='activitytimeentrymodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activitytimeentry_user', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterUniqueTogether(
            name='activitytimeentrymodel',
            unique_together={('user', 'activity', 'completed_at_date')},
        ),
    ]
