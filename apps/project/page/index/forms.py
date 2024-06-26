import uuid

from django import forms

from .models import ContactModel


class ContactForm(forms.ModelForm):

    names = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'maxlength': 150,
                'placeholder': 'Names',
                'class': 'form-control',
                'name': 'names'
            }
        ),
        required=True
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'maxlength': 254,
                'placeholder': 'Email',
                'class': 'form-control',
                'name':'email'
            }
        ),
        required=True
    )

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'contact_title',
                'maxlength': 150,
                'placeholder': 'Subject',
                'class': 'form-control'
            }
        ),
        required=True
    )

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Message',
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
