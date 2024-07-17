from django.conf import settings
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView, View, edit

from apps.common.utils.contrib.auth.mixins import LoginGroupRequiredMixin

from .forms import UserLoginForm, UserRegisterForm

UserModel = get_user_model()


class SpiritIndexTemplateView(LoginGroupRequiredMixin, TemplateView):
    template_name = 'spirit/spirit_index.html'
    group_required = settings.SPIRIT_PERMISSION_GROUP_NAME
    redirect_url = reverse_lazy('spirit_core:login')


class SpiritUserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'spirit_core:login'
            )
        )


class SpiritUserLoginFormView(edit.FormView):
    template_name = "spirit/account/login.html"
    form_class = UserLoginForm
    group_required = settings.SPIRIT_PERMISSION_GROUP_NAME

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.groups.filter(name=self.group_required).exists():
            return redirect('spirit_core:index')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        remember_me = form.cleaned_data['remember_me']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)

            if remember_me:
                self.request.session.set_expiry(None)
            else:
                self.request.session.set_expiry(7200)

            return super(SpiritUserLoginFormView, self).form_valid(form)
        else:
            form.add_error(None, _("Username or Password incorrect"))
            return self.form_invalid(form)

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse('spirit_core:index')


class SpiritUserRegisterFormView(edit.FormView):
    template_name = "spirit/account/register.html"
    form_class = UserRegisterForm
    group_required = settings.SPIRIT_PERMISSION_GROUP_NAME

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.groups.filter(name=self.group_required).exists():
            return redirect('spirit_core:index')
        return super().dispatch(request, *args, **kwargs)

    def send_activation_email(self, user):
        token = default_token_generator.make_token(user)

        uid = urlsafe_base64_encode(force_bytes(user.pk))

        activation_link = self.request.build_absolute_uri(
            reverse(
                'spirit_core:activate',
                kwargs={
                    'uidb64': uid, 'token': token
                }
            )
        )

        mail_subject = _('Activate your Spirit account')

        html_message = render_to_string(
            'spirit/account/email/activation_email.html',
            {
                'user': user,
                'domain': get_current_site(self.request).domain,
                'uid': uid,
                'token': token,
                'activation_link': activation_link,
            }
        )

        plain_message = strip_tags(html_message)

        send_mail(
            mail_subject,
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            html_message=html_message,
            fail_silently=False
        )

    def form_valid(self, form):
        user = UserModel.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            employee_id=form.cleaned_data['employee_id'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            password=form.cleaned_data['password'],
            cell_phone=form.cleaned_data['cell_phone'],
            birthday=form.cleaned_data['birthday'],
            privacy=form.cleaned_data['privacy']
        )
        user.is_active = False
        user.save()

        self.send_activation_email(user)

        return render(self.request, 'spirit/account/confirm_email.html', {'new_user_email': user.email})

    def get_success_url(self):
        return reverse('spirit_core:index')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserModel.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        group = Group.objects.get(name=settings.SPIRIT_PERMISSION_GROUP_NAME)
        user.groups.add(group)
        return redirect(f'{reverse_lazy("spirit_core:login")}?login_username={user.username}')
    else:
        return render(request, 'spirit/account/activate_unsuccessfully.html')
