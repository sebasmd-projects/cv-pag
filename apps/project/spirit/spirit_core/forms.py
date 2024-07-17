from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from apps.project.common.users.validators import (UnicodeLastNameValidator,
                                                  UnicodeNameValidator,
                                                  UnicodeUsernameValidator)
from .validators import CompanyEmailValidator

UserModel = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(
        label=_('User - Email - Employee ID'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'login_username',
                'type': 'text',
                'placeholder': _('User, Email or Employee ID'),
                'class': 'form-control',
                'aria-label': _('User, Email or Employee ID'),
                'aria-describedby': 'login_username'
            },
        )
    )

    password = forms.CharField(
        label=_('Password'),
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'id': 'login_password',
                'type': 'password',
                'placeholder': _('Password'),
                'class': 'form-control',
                'aria-label': _('Password'),
                'aria-describedby': 'login_password'
            }
        )
    )

    remember_me = forms.BooleanField(
        label=_('Remember me'),
        required=False,
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                'id': 'login_remember_me',
                'type': 'checkbox',
                'class': 'form-check-input',
            }
        )
    )

    def clean(self):
        cleaned_data = super(UserLoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if username and password:
            if not authenticate(username=username, password=password):
                self.add_error(
                    'password',
                    _('Las credenciales son inválidas')
                )

        return cleaned_data


class UserRegisterForm(forms.ModelForm):
    username_validator = UnicodeUsernameValidator()
    name_validator = UnicodeNameValidator()
    last_name_validator = UnicodeLastNameValidator()
    company_email_validator = CompanyEmailValidator()
    username = forms.CharField(
        label=_("Username"),
        validators=[username_validator],
        required=True,
        widget=forms.TextInput(
            attrs={
                "id": "register_username",
                "type": "text",
                "placeholder": _("Username"),
                "class": "form-control",
                'aria-label': _('Username'),
                'aria-describedby': 'register_username'
            }
        )
    )

    email = forms.CharField(
        label=_("Email"),
        validators=[company_email_validator],
        required=True,
        widget=forms.EmailInput(
            attrs={
                "id": "register_email",
                "type": "email",
                "placeholder": _("Email"),
                "class": "form-control",
                'aria-label': _('Email'),
                'aria-describedby': 'register_email'
            }
        )
    )

    employee_id = forms.IntegerField(
        label=_("Employee ID"),
        required=True,
        widget=forms.NumberInput(
            attrs={
                "id": "register_employee_id",
                "type": "number",
                "placeholder": _("Employee ID"),
                "class": "form-control",
                'aria-label': _('Employee ID'),
                'aria-describedby': 'register_employee_id'
            }
        )
    )

    password = forms.CharField(
        label=_('Password'),
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "id": "register_password",
                'type': 'password',
                'placeholder': _('Password'),
                'class': 'form-control',
                'aria-label': _('Password'),
                'aria-describedby': 'register_password'
            }
        )
    )

    confirm_password = forms.CharField(
        label=_('Repeat password'),
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "id": "register_confirm_password",
                "type": "password",
                "placeholder": _('Repeat password'),
                "class": "form-control",
                'aria-label': _('Repeat password'),
                'aria-describedby': 'register_confirm_password'
            }
        )
    )

    first_name = forms.CharField(
        label=_("Names"),
        required=True,
        validators=[name_validator],
        widget=forms.TextInput(
            attrs={
                "id": "register_first_name",
                "type": "text",
                "placeholder": _("Names"),
                "class": "form-control",
                'aria-label': _('Names'),
                'aria-describedby': 'register_first_name'
            }
        )
    )

    last_name = forms.CharField(
        label=_("Last name"),
        required=True,
        validators=[last_name_validator],
        widget=forms.TextInput(
            attrs={
                "id": "register_last_name",
                "type": "text",
                "placeholder": _("Last name"),
                "class": "form-control",
                'aria-label': _('Last name'),
                'aria-describedby': 'register_last_name'
            }
        )
    )

    cell_phone = forms.CharField(
        label=_("Cellphone"),
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'register_phone',
                'type': 'tel',
                'placeholder': _('Cellphone'),
                'class': 'form-control',
                'aria-describedby': 'register_phone',
                'aria-label': _('Cellphone')
            }
        )
    )

    birthday = forms.DateField(
        label=_("Birthday"),
        required=False,
        widget=forms.NumberInput(
            attrs={
                'id': 'register_birthday',
                'type': 'date',
                'placeholder': _('Birthday'),
                'class': 'form-control',
                'aria-describedby': 'register_birthday',
                'aria-label': _('Birthday')
            }
        )
    )

    privacy = forms.BooleanField(
        label=_('Terms and Conditions'),
        required=True,
        widget=forms.CheckboxInput(
            attrs={
                'id': 'register_privacy_policy',
                'type': 'checkbox',
                'class': 'form-check-input',
                'aria-describedby': 'register_privacy_policy',
                'aria-label': _('Terms and Conditions')
            }
        )
    )

    def clean_confirm_password(self):
        validate_password(
            self.cleaned_data["password"],
        )

        validate_password(
            self.cleaned_data["confirm_password"],
        )

        if self.cleaned_data["password"] != self.cleaned_data["confirm_password"]:
            raise ValidationError(_('Passwords do not match'))

    class Meta:
        model = UserModel
        fields = (
            "username",
            "email",
            "employee_id",
            "first_name",
            "last_name",
            "cell_phone",
            "birthday",
            "privacy"
        )


class UserUpdateProfile(forms.ModelForm):
    pass
