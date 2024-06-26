from django.urls import path
from .views import IndexTemplateView, ContactFormView

app_name = "index"

urlpatterns = [
    path(
        '',
        IndexTemplateView.as_view(),
        name='home'
    ),
    path(
        'contact/',
        ContactFormView.as_view(),
        name='contact'
    )
]