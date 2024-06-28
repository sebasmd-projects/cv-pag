import uuid

from django import forms

from .models import ContactModel
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.ModelForm):

    names = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Names'),
                'maxlength': 150,
                'class': 'form-control',
                'name': 'names'
            }
        ),
        required=True
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': _('Email'),
                'maxlength': 254,
                'class': 'form-control',
                'name':'email'
            }
        ),
        required=True
    )

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Subject'),
                'id': 'contact_title',
                'maxlength': 150,
                'class': 'form-control'
            }
        ),
        required=True
    )

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': _('Message'),
                'class': 'form-control',
                'name':'message',
                'rows':'3'
            }
        ),
        required=True
    )

    unique_id = forms.UUIDField(
        widget=forms.HiddenInput(),
        initial=uuid.uuid4,
    )

    class Meta:
        model = ContactModel
        fields = ['names', 'email', 'title', 'message', 'unique_id']
