from django.urls import path

from .views import RamptwoTemplateView

app_name = 'ramptwo'

urlpatterns = [
    path(
        'ramptwo',
        RamptwoTemplateView.as_view(),
        name='ramptwo'
    )
]
