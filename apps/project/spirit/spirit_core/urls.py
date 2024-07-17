from django.urls import path

from .views import SpiritIndexTemplateView

app_name = "spirit_core"

urlpatterns = [
    path(
        '',
        SpiritIndexTemplateView.as_view(),
        name="index"
    )
]
