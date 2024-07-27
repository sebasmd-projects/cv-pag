from django import forms

from .models import RampDataModel

class RampDataModelForm(forms.ModelForm):
    class Meta:
        model = RampDataModel
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'winery_1_open': forms.TimeInput(attrs={'type': 'time'}),
            'winery_1_closure': forms.TimeInput(attrs={'type': 'time'}),
            'first_unloading_of_luggage': forms.TimeInput(attrs={'type': 'time'}),
            'last_unloading_of_luggage': forms.TimeInput(attrs={'type': 'time'}),
            'arrival_of_the_first_baggage_shipping': forms.TimeInput(attrs={'type': 'time'}),
            'arrival_of_the_last_baggage_shipping': forms.TimeInput(attrs={'type': 'time'}),
            'rear_ladder_coupling_begins': forms.TimeInput(attrs={'type': 'time'}),
            'rear_ladder_coupling_end': forms.TimeInput(attrs={'type': 'time'}),
            'maintenance_arrival': forms.TimeInput(attrs={'type': 'time'}),
            'maintenance_output': forms.TimeInput(attrs={'type': 'time'}),
            'gasoline_arrival': forms.TimeInput(attrs={'type': 'time'}),
            'gasoline_output': forms.TimeInput(attrs={'type': 'time'}),
            'firefighters_in': forms.TimeInput(attrs={'type': 'time'}),
            'firefighters_out': forms.TimeInput(attrs={'type': 'time'}),
            'plant_coupling': forms.TimeInput(attrs={'type': 'time'}),
            'plant_decoupling': forms.TimeInput(attrs={'type': 'time'}),
            'airplane_tire_lock': forms.TimeInput(attrs={'type': 'time'}),
            'airplane_push_back': forms.TimeInput(attrs={'type': 'time'}),
            'taxiing': forms.TimeInput(attrs={'type': 'time'}),
        }