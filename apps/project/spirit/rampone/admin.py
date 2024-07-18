from django.contrib import admin

from .models import (ActivityNamesCheckListModel, ActivityTimeEntryModel,
                     FlightModel, RampDataModel, UserActivityCheckListModel)

admin.site.register(ActivityNamesCheckListModel)
admin.site.register(ActivityTimeEntryModel)
admin.site.register(UserActivityCheckListModel)
admin.site.register(RampDataModel)
admin.site.register(FlightModel)
