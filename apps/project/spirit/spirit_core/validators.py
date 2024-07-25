from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class CompanyEmailValidator(validators.RegexValidator):
    regex = r'^[\w\.-]+@(spirit\.com|longportsecurity\.com|sebasmoralesd\.com)$'
    message = _(
        "Please enter a valid email address. The email should be from the domains @spirit.com or @longportsecurity .com."
    )
    flags = 0
