from django.urls import path

from .views import BaggageTemplateView

app_name = 'baggage'

urlpatterns = [
    path(
        'baggage',
        BaggageTemplateView.as_view(),
        name='baggage'
    )
]
