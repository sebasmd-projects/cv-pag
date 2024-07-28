from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from app_core import get_app_from_path
from apps.project.spirit.spirit_core.models import FlightModel

TimeStampedModel = get_app_from_path(
    f'{settings.UTILS_PATH}.models.TimeStampedModel'
)

UserModel = get_user_model()


class BaggageShippingModel(TimeStampedModel):
    agent = models.ForeignKey(
        UserModel,
        verbose_name=_("Agent"),
        on_delete=models.CASCADE,
        related_name='baggageshipping_user',
    )

    flight = models.ForeignKey(
        FlightModel,
        verbose_name=_("Flight"),
        related_name="gaggageshipping_flight",
        on_delete=models.CASCADE
    )

    cart_name = models.CharField(
        _("cart name"),
        max_length=50,
        default=_('diligence ')
    )

    cart_code = models.CharField(
        _("cart code"),
        max_length=5
    )

    cart_number = models.PositiveIntegerField(
        _("cart number")
    )

    total_baggage = models.PositiveIntegerField(
        _("total baggage")
    )

    def __str__(self):
        return f"{self.cart_code} - {self.cart_number}"

    class Meta:
        db_table = 'apps_project_spirit_baggage_shipping'
        verbose_name = _('2.0 Baggage Shipping')
        verbose_name_plural = _('2.0 Baggage Shippings')


class BaggageShippingSealsModel(TimeStampedModel):
    seal_number = models.PositiveIntegerField(
        _("seal number")
    )

    diligence = models.ForeignKey(
        BaggageShippingModel,
        verbose_name=_("baggage shipping"),
        on_delete=models.CASCADE,
        related_name='baggageshippingseals_baggageshipping'
    )

    def __str__(self):
        return f"{self.diligence.cart_code} - {self.diligence.cart_number} | {self.seal_number}"

    class Meta:
        db_table = 'apps_project_spirit_baggage_shipping_seals'
        verbose_name = _('2.1 Seal')
        verbose_name_plural = _('2.1 Seals')
