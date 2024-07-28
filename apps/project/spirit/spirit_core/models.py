from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from app_core import get_app_from_path

TimeStampedModel = get_app_from_path(
    f'{settings.UTILS_PATH}.models.TimeStampedModel'
)


class FlightModel(TimeStampedModel):
    flight_category_choices = [
        (None, _('Select One')),
        ("D", _('Departure')),
        ("A", _('Arrival'))
    ]

    flight_category = models.CharField(
        _("category"),
        choices=flight_category_choices,
        max_length=50,
        default=flight_category_choices[1]
    )

    flight_name = models.CharField(
        _("Flight name"),
        max_length=10,
        blank=True, null=True
    )

    flight_number = models.PositiveIntegerField(
        _("Flight number"),
        blank=True, null=True
    )

    def __str__(self):
        return f"{self.get_flight_category_display()} {self.flight_name} {self.flight_number}"

    class Meta:
        db_table = 'apps_project_spirit_flight'
        verbose_name = _('1.0 Flight')
        verbose_name_plural = _('1.0 Flights')
        unique_together = ['flight_category', 'flight_name', 'flight_number']
