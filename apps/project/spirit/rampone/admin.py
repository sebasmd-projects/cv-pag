from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from .models import (ActivityNamesCheckListModel, ActivityTimeEntryModel,
                     FlightModel, RampDataModel, UserActivityCheckListModel)


@admin.register(ActivityNamesCheckListModel)
class ActivityNamesCheckListModelAdmin(SortableAdminMixin, admin.ModelAdmin):
    ordering = ['default_order']


admin.site.register(ActivityTimeEntryModel)
admin.site.register(UserActivityCheckListModel)
admin.site.register(RampDataModel)
admin.site.register(FlightModel)
