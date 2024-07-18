from django.urls import path

from .views import RampOneCheckListTemplateView

app_name = 'rampone'

urlpatterns = [
    path(
        'rampone',
        RampOneCheckListTemplateView.as_view(),
        name='rampone'
    )
]
