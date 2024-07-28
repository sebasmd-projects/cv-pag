from adminsortable2.admin import SortableAdminMixin
from django import forms
from django.contrib import admin


from .models import (ActivityNamesCheckListModel, ActivityTimeEntryModel,
                     FlightModel, RampDataModel, UserActivityCheckListModel)


class RampDataModelAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['flight_departure'].queryset = FlightModel.objects.filter(
            flight_category='D'
        )

        self.fields['flight_arrival'].queryset = FlightModel.objects.filter(
            flight_category='A'
        )

    class Meta:
        model = RampDataModel
        fields = '__all__'


@admin.register(ActivityNamesCheckListModel)
class ActivityNamesCheckListModelAdmin(SortableAdminMixin, admin.ModelAdmin):
    ordering = ['default_order']


@admin.register(RampDataModel)
class RampDataModelAdmin(admin.ModelAdmin):
    form = RampDataModelAdminForm


admin.site.register(ActivityTimeEntryModel)
admin.site.register(UserActivityCheckListModel)
admin.site.register(FlightModel)
