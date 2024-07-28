from django import forms
from django.utils.translation import gettext_lazy as _

from .models import FlightModel, RampDataModel


class RampDataModelForm(forms.ModelForm):
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
        fields = [
            'agent', 'date', 'flight_arrival',
            'flight_departure', 'license_plate',
            'winery_1_open', 'winery_1_closure',
            'first_unloading_of_luggage',
            'last_unloading_of_luggage',
            'arrival_of_the_first_baggage_shipping',
            'arrival_of_the_last_baggage_shipping',
            'rear_ladder_coupling_begins',
            'rear_ladder_coupling_end',
            'maintenance_arrival', 'maintenance_output',
            'gasoline_arrival', 'gasoline_output',
            'firefighters_in', 'firefighters_out',
            'plant_coupling', 'plant_decoupling',
            'baggage_load_cp1', 'airplane_tire_lock',
            'airplane_push_back', 'taxiing'
        ]
        widgets = {
            'flight_arrival': forms.Select(
                attrs={
                    'class': 'form-select',
                    'aria-label': _('Flight Arrival')
                }
            ),
            'flight_departure': forms.Select(
                attrs={
                    'class': 'form-select',
                    'aria-label': _('Flight Departure')
                }
            )
        }
