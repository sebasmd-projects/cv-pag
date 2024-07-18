from django import forms

from .models import ActivityNamesCheckListModel, ActivityTimeEntryModel

class ActivityCheckListForm(forms.ModelForm):
    class Meta:
        model = ActivityNamesCheckListModel
        fields = ['name']

class HiddenActivityTimeEntryForm(forms.ModelForm):
    class Meta:
        model = ActivityTimeEntryModel
        fields = ['activity', 'completed_at']
        widgets = {
            'activity': forms.HiddenInput(),
            'completed_at': forms.HiddenInput(),
        }