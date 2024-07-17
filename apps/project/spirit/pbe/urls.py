from django.urls import path

from .views import PBETemplateView

app_name = 'pbe'

urlpatterns = [
    path(
        'pbe',
        PBETemplateView.as_view(),
        name='pbe'
    )
]
