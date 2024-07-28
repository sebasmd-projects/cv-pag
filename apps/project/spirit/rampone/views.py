from datetime import datetime

from django.conf import settings
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.timezone import localtime
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView

from apps.common.utils.contrib.auth.mixins import LoginGroupRequiredMixin

from .forms import RampDataModelForm
from .models import (ActivityNamesCheckListModel, ActivityTimeEntryModel,
                     RampDataModel, UserActivityCheckListModel)


class RampOneCheckListTemplateView(LoginGroupRequiredMixin, TemplateView):
    template_name = 'rampone_base.html'
    group_required = settings.SPIRIT_PERMISSION_GROUP_NAME
    redirect_url = reverse_lazy('spirit_core:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        activities = ActivityNamesCheckListModel.objects.all()
        entries = ActivityTimeEntryModel.objects.filter(
            user=user, completed_at_date=timezone.now().date()
        )
        entries_dict = {entry.activity_id: entry for entry in entries}
        context['activities'] = activities
        context['entries_dict'] = entries_dict

        current_datetime = localtime(timezone.now())
        today_date = current_datetime.date()
        today_time = current_datetime.time()
        context['today_date'] = today_date.strftime('%Y-%m-%d')
        context['today_time'] = today_time.strftime('%H:%M')

        try:
            ramp_data_instance = RampDataModel.objects.get(
                agent=user, date=today_date)
            context['ramp_data_form'] = RampDataModelForm(
                instance=ramp_data_instance)
        except RampDataModel.DoesNotExist:
            context['ramp_data_form'] = RampDataModelForm()

        return context

    def post(self, request, *args, **kwargs):
        if 'activity_id' in request.POST:
            return self.handle_activity_form(request)
        elif 'data_form' in request.POST:
            return self.handle_ramp_data_form(request)

    def handle_activity_form(self, request):
        activity_id = request.POST.get('activity_id')
        local_time_str = request.POST.get('local_time')
        local_date_str = request.POST.get('local_date')

        if activity_id and local_time_str and local_date_str:
            user = request.user
            activity = ActivityNamesCheckListModel.objects.get(id=activity_id)
            current_date = datetime.strptime(local_date_str, '%m/%d/%Y').date()
            current_time = datetime.strptime(local_time_str, '%H:%M:%S').time()

            entry, created = ActivityTimeEntryModel.objects.get_or_create(
                user=user,
                activity=activity,
                completed_at_date=current_date,
                defaults={'completed_at_time': current_time, 'completed': True}
            )
            if not created:
                if entry.completed:
                    return JsonResponse({'error': _('Activity already completed today.')}, status=400)
                entry.completed_at_time = current_time
                entry.completed = True
                entry.save()

            user_checklist, created = UserActivityCheckListModel.objects.get_or_create(
                user=user
            )

            user_checklist.time_entries.add(entry)

            return JsonResponse({'success': True, 'activity_id': activity_id, 'completed_at_time': current_time.strftime('%H:%M')})

    def handle_ramp_data_form(self, request):
        local_date_str = request.POST.get('local_date')
        local_time_str = request.POST.get('local_time')
        data_form = request.POST.get('data_form')

        if local_date_str and local_time_str and data_form:
            form = RampDataModelForm(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'error': form.errors}, status=400)
        return JsonResponse({'success': True})
