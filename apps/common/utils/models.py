from auditlog.models import AuditlogHistoryField
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

utils_path: str = settings.UTILS_PATH
utils_db_name = utils_path.replace('.', '_')


class TimeStampedModel(models.Model):
    """A base model class with timestamp fields."""
    history = AuditlogHistoryField()

    language_choices = [
        ('es', _('Spanish')),
        ('en', _('English')),
    ]

    language = models.CharField(
        _("language"),
        max_length=4,
        choices=language_choices,
        default='es',
        blank=True,
        null=True
    )

    created = models.DateTimeField(
        _('created'),
        default=timezone.now,
        editable=False
    )

    updated = models.DateTimeField(
        _('updated'),
        auto_now=True,
        editable=False
    )

    is_active = models.BooleanField(
        _("is active"),
        default=True
    )

    default_order = models.PositiveIntegerField(
        _('priority'),
        default=1,
        blank=True,
        null=True
    )

    class Meta:
        abstract = True
        ordering = ['default_order']


class RequestLogModel(TimeStampedModel):
    """A model to log requests."""
    requests = models.JSONField(
        _("requests"),
        blank=True,
        null=True,
        default=dict
    )

    @classmethod
    def get_instance(cls):
        """Get the singleton instance of RequestLogModel."""
        instance, _ = cls.objects.get_or_create(id=1)
        return instance

    def add_request_entry(self, entry):
        """Add a request entry to the log.

        :param entry: The request entry to add.
        :type entry: dict
        """
        requests = self.requests or []
        requests.insert(0, entry)
        self.requests = requests
        self.save()

    def __str__(self) -> str:
        return f'{self.id}'

    class Meta:
        db_table = f'{utils_db_name}_requestlog'
        verbose_name = _('Request')
        verbose_name_plural = _('Requests')
