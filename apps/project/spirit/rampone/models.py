from auditlog.registry import auditlog
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from app_core import get_app_from_path

TimeStampedModel = get_app_from_path(
    f'{settings.UTILS_PATH}.models.TimeStampedModel'
)

UserModel = get_user_model()


class ActivityNamesCheckListModel(TimeStampedModel):
    name = models.CharField(_("activity"), max_length=50)
    description = models.TextField(_("description"), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'apps_project_spirit_activities'
        verbose_name = _('1.1 Activity')
        verbose_name_plural = _('1.1 Activities')


class ActivityTimeEntryModel(TimeStampedModel):
    user = models.ForeignKey(UserModel, verbose_name=_("user"), on_delete=models.CASCADE, related_name='activitytimeentry_user')
    activity = models.ForeignKey(ActivityNamesCheckListModel, verbose_name=_("activity"), on_delete=models.CASCADE, related_name='activitytimeentry_activity')
    completed_at_date = models.DateField(_("completed date"))
    completed_at_time = models.TimeField(_("completed time"))
    completed = models.BooleanField(_("completed"), default=False)
    
    def __str__(self):
        completed_at_date_formatted = self.completed_at_date.strftime(
            "%B/%d/%Y"
        )
        completed_at_time_formatted = self.completed_at_time.strftime(
            "%H:%M"
        )
        return f"{self.user.get_full_name()} | {self.activity.name} | {completed_at_date_formatted} {completed_at_time_formatted}"

    class Meta:
        db_table = 'apps_project_spirit_activity_time_entry'
        verbose_name = _('1.2 Activity time entry')
        verbose_name_plural = _('1.2 Activity time entries')
        unique_together = ['user', 'activity', 'completed_at_date']


class UserActivityCheckListModel(TimeStampedModel):
    user = models.ForeignKey(
        UserModel,
        verbose_name=_("user"),
        on_delete=models.SET_NULL,
        null=True,
        related_name='useractivitychecklist_user'
    )

    time_entries = models.ManyToManyField(
        ActivityTimeEntryModel,
        blank=True
    )

    def __str__(self):
        return f"{self.user.get_full_name()}"

    class Meta:
        db_table = 'apps_project_spirit_user_activity_check_list'
        verbose_name = _('1.0 CheckList')
        verbose_name_plural = _('1.0 CheckList')


class FlightModel(TimeStampedModel):
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
        return f"{self.flight_name} {self.flight_number}"

    class Meta:
        db_table = 'apps_project_spirit_flight'
        verbose_name = _('2.1 Flight')
        verbose_name_plural = _('2.1 Flights')


class RampDataModel(TimeStampedModel):

    agent = models.ForeignKey(
        UserModel,
        verbose_name=_("Agent"),
        on_delete=models.CASCADE,
        related_name='rampdata_user'
    )

    date = models.DateField(
        _("Date"),
        default=timezone.now,
    )

    flight_arrival = models.ForeignKey(
        FlightModel,
        verbose_name=_("Flight arrival"),
        related_name="flight_arrival",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    flight_departure = models.ForeignKey(
        FlightModel,
        verbose_name=_("Flight departure"),
        related_name="flight_departure",
        on_delete=models.SET_NULL,
        null=True
    )

    license_plate = models.CharField(
        _("license plate"),
        max_length=10
    )

    winery_1_open = models.TimeField(
        _("winery 1 open")
    )

    winery_1_closure = models.TimeField(
        _("winery 1 clousure")
    )

    first_unloading_of_luggage = models.TimeField(
        _("first unloading of luggage")
    )

    last_unloading_of_luggage = models.TimeField(
        _("last unloading of luggage")
    )

    arrival_of_the_first_baggage_shipping = models.TimeField(
        _("arrival of the first baggage shipping")
    )

    arrival_of_the_last_baggage_shipping = models.TimeField(
        _("arrival of the last baggage shipping")
    )

    rear_ladder_coupling_begins = models.TimeField(
        _("rear ladder coupling begins"),
        auto_now=True
    )

    rear_ladder_coupling_end = models.TimeField(
        _("rear ladder coupling begins"),
        auto_now=True
    )

    maintenance_arrival = models.TimeField(
        _("maintenance arrival"),
        auto_now=True
    )

    maintenance_output = models.TimeField(
        _("maintenance output"),
        auto_now=True
    )

    gasoline_arrival = models.TimeField(
        _("terpel arrival"),
        auto_now=True
    )

    gasoline_output = models.TimeField(
        _("terpel output"),
        auto_now=True
    )

    firefighters_in = models.TimeField(
        _("firefighters in")
    )

    firefighters_out = models.TimeField(
        _("firefighters out")
    )

    plant_coupling = models.TimeField(
        _("plant coupling")
    )

    plant_decoupling = models.TimeField(
        _("plant decoupling")
    )

    baggage_load_cp1 = models.PositiveIntegerField(
        _("baggage load cp1")
    )

    airplane_tire_lock = models.TimeField(
        _("airplane tire lock")
    )

    airplane_push_back = models.TimeField(
        _("airplane push back")
    )

    # Diligencia 1
    baggage_shipping_1 = models.CharField(
        _("baggage shipping 1 code and number"),
        max_length=10
    )

    baggage_shipping_1_total = models.PositiveIntegerField(
        _("baggage shipping 1 total")
    )

    seals_shipping_1 = models.CharField(
        _("seals shipping 1"),
        max_length=255
    )

    # Diligencia 2
    baggage_shipping_2 = models.CharField(
        _("baggage shipping 2 code and number"),
        max_length=10,
        blank=True, null=True
    )

    baggage_shipping_2_total = models.PositiveIntegerField(
        _("baggage shipping 2 total"),
        blank=True, null=True
    )

    seals_shipping_2 = models.CharField(
        _("seals shipping 2"),
        max_length=255,
        blank=True, null=True
    )

    # Diligencia 3
    baggage_shipping_3 = models.CharField(
        _("baggage shipping 3 code and number"),
        max_length=10,
        blank=True, null=True
    )

    baggage_shipping_3_total = models.PositiveIntegerField(
        _("baggage shipping 3 total"),
        blank=True, null=True
    )

    seals_shipping_3 = models.CharField(
        _("seals shipping 3"),
        max_length=255,
        blank=True, null=True
    )

    # Diligencia 4
    baggage_shipping_4 = models.CharField(
        _("baggage shipping 4 code and number"),
        max_length=10,
        blank=True, null=True
    )

    baggage_shipping_4_total = models.PositiveIntegerField(
        _("baggage shipping 4 total"),
        blank=True, null=True
    )

    seals_shipping_4 = models.CharField(
        _("seals shipping 4"),
        max_length=255,
        blank=True, null=True
    )

    taxiing = models.TimeField(
        _("taxiing")
    )

    def save(self, *args, **kwargs):
        if self.flight_arrival and not self.flight_departure:
            if self.flight_arrival.flight_number == 1473:
                self.flight_departure, _ = FlightModel.objects.get_or_create(
                    flight_name="MCO",
                    flight_number=1474
                )
            elif self.flight_arrival.flight_number == 235:
                self.flight_departure, _ = FlightModel.objects.get_or_create(
                    flight_name="FLL",
                    flight_number=236
                )

        elif self.flight_departure and not self.flight_arrival:
            if self.flight_departure.flight_number == 1474:
                self.flight_arrival, _ = FlightModel.objects.get_or_create(
                    flight_name="MCO",
                    flight_number=1473
                )
            elif self.flight_departure.flight_number == 236:
                self.flight_arrival, _ = FlightModel.objects.get_or_create(
                    flight_name="FLL",
                    flight_number=235
                )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{_('Ramp 1')} - {self.flight_departure.flight_name}"

    class Meta:
        db_table = 'apps_project_spirit_ramp_one_data'
        verbose_name = _('2.0 Ramp One Data')
        verbose_name_plural = _('2.0 Ramp One Data')


auditlog.register(
    RampDataModel,
    serialize_data=True
)
