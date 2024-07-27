import uuid
from datetime import date

from auditlog.registry import auditlog
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_delete, post_save, pre_save
from django.utils.translation import gettext_lazy as _

from app_core import get_app_from_path

from .signals import (auto_delete_profile_photo_on_change,
                      auto_delete_profile_photo_on_delete,
                      avatar_directory_path, optimize_image)

TimeStampedModel = get_app_from_path(
    f'{settings.UTILS_PATH}.models.TimeStampedModel'
)


class UserModel(TimeStampedModel, AbstractUser):
    id = models.UUIDField(
        'ID',
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        serialize=False,
        editable=False
    )

    employee_id = models.PositiveIntegerField(
        blank=True,
        null=True,
        unique=True,
    )

    profile_photo = models.ImageField(
        _("profile picture"),
        upload_to=avatar_directory_path,
        blank=True,
        null=True
    )

    cell_phone = models.CharField(
        _('cell_phone'),
        max_length=15,
        null=True,
        blank=True
    )

    birthday = models.DateField(
        _('birthday'),
        default=date.today,
        blank=True,
        null=True
    )

    REQUIRED_FIELDS = [
        'email',
        'first_name',
        'last_name'
    ]

    country_code = models.CharField(
        _('country code'),
        max_length=10,
        blank=True,
        null=True,
        default='CO'
    )

    privacy = models.BooleanField(
        _('terms and conditions'),
        default=False
    )

    def get_age(self):
        return date.today().year - self.birthday.year - (
            (date.today().month, date.today().day) < (
                self.birthday.month, self.birthday.day)
        )

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        self.username = self.username.lower()

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.get_full_name()}"

    class Meta:
        db_table = 'apps_project_common_users_user'
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        unique_together = [['email', 'employee_id'], ['cell_phone', 'email'], ['username', 'email']]


post_save.connect(optimize_image, sender=UserModel)
post_delete.connect(auto_delete_profile_photo_on_delete, sender=UserModel)
pre_save.connect(auto_delete_profile_photo_on_change, sender=UserModel)

auditlog.register(
    UserModel,
    serialize_data=True
)
