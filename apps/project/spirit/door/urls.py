from django.urls import path

from .views import DoorTemplateView

app_name = 'door'

urlpatterns = [
    path(
        'door',
        DoorTemplateView.as_view(),
        name='door'
    )
]
