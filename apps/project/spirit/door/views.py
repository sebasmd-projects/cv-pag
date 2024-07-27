from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from apps.common.utils.contrib.auth.mixins import LoginGroupRequiredMixin


class DoorTemplateView(LoginGroupRequiredMixin, TemplateView):
    template_name = 'door_base.html'
    group_required = settings.SPIRIT_PERMISSION_GROUP_NAME
    redirect_url = reverse_lazy('spirit_core:login')
