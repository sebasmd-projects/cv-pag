from django.shortcuts import redirect, render
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView, View

from .models import ActivityNamesCheckListModel, ActivityTimeEntryModel, UserActivityCheckListModel


class RampOneCheckListTemplateView(TemplateView):
    template_name = 'rampone_base.html'

    def get(self, request):
        activities = ActivityNamesCheckListModel.objects.all()
        return render(request, self.template_name, {'activities': activities})
    
    def post(self, request):
        activity_id = request.POST.get('activity_id')
        if activity_id:
            activity = ActivityNamesCheckListModel.objects.get(id=activity_id)
            completed_at = timezone.now()
            time_entry = ActivityTimeEntryModel.objects.create(activity=activity, completed_at=completed_at)
            
            user_checklist, created = UserActivityCheckListModel.objects.get_or_create(user=request.user)
            user_checklist.time_entries.add(time_entry)
            
        return redirect('rampone:rampone')