from datetime import date, time

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
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
        context['ramp_data_form'] = RampDataModelForm()
        
        return context

    def post(self, request, *args, **kwargs):
        activity_id = request.POST.get('activity_id')
        if activity_id:
            user = request.user
            activity = ActivityNamesCheckListModel.objects.get(id=activity_id)
            current_date = timezone.now().date()
            current_time = timezone.now().time()
            
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
        
    def patch(self, request, *args, **kwargs):
        user = request.user
        activity_id = request.POST.get('activity_id')
        activity = ActivityNamesCheckListModel.objects.get(id=activity_id)
        current_date = timezone.now().date()
        entry = ActivityTimeEntryModel.objects.filter(
            user=user, activity=activity, completed_at_date=current_date).first()

        if entry:
            if entry.completed:
                return JsonResponse({'error': _('Activity already completed today.')}, status=400)
            entry.completed = not entry.completed
            entry.completed_at_time = timezone.now().time() if entry.completed else None
            entry.save()
        else:
            ActivityTimeEntryModel.objects.create(
                user=user,
                activity=activity,
                completed_at_date=current_date,
                completed_at_time=timezone.now().time(),
                completed=True
            )
        return JsonResponse({'success': True, 'activity_id': activity_id, 'completed': entry.completed})

