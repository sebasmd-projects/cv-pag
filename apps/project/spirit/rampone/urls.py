from django.urls import path

from .views import RamponeTemplateView

app_name = 'rampone'

urlpatterns = [
    path(
        'rampone',
        RamponeTemplateView.as_view(),
        name='rampone'
    )
]
