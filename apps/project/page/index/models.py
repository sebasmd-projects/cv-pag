import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from app_core import get_app_from_path

TimeStampedModel = get_app_from_path(
    f'{settings.UTILS_PATH}.models.TimeStampedModel'
)


class ContactModel(TimeStampedModel):
    names = models.CharField(
        _('names'),
        max_length=150
    )

    email = models.EmailField(
        _("email"),
        max_length=254
    )

    title = models.CharField(
        _("subject"),
        max_length=50
    )

    message = models.TextField(
        _("message")
    )

    unique_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True
    )

    def __str__(self):
        return self.title
