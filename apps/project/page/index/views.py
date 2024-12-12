from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils import translation
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView, edit
from honeypot.decorators import check_honeypot

from .forms import ContactForm
from .models import ContactModel


class IndexTemplateView(TemplateView):
    template_name = 'project/page/index/templates/page/index.html'


@method_decorator(check_honeypot, name='post')
class ContactFormView(edit.FormView):
    form_class = ContactForm
    success_url = reverse_lazy('index:home')
    template_name = "project/page/index/templates/sections/contact/form.html"

    def form_valid(self, form):
        unique_id = form.cleaned_data.get('unique_id')
        honeypot_field = form.cleaned_data.get('mail_validation')

        if honeypot_field:
            form.save()
            return super().form_valid(form)

        if ContactModel.objects.filter(unique_id=unique_id).exists():
            form.add_error(None, _("This form has already been sent."))
            return self.form_invalid(form)

        contact = form.save()

        user_language = self.request.LANGUAGE_CODE

        html_message = render_to_string('project/page/index/templates/sections/contact/contact_email_template.html', {
            'names': contact.names,
            'LANGUAGE_CODE': user_language,
        })

        subject = _('Message Received! | sebasmoralesd.com')
        plain_message = _('Thank you %(name)s for contacting me.') % {
            'name': contact.names}

        send_mail(
            subject=subject,
            message=plain_message,
            html_message=html_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[contact.email],
            fail_silently=False
        )

        return super().form_valid(form)