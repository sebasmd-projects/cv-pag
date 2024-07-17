from django.urls import path

from .views import (SpiritIndexTemplateView, SpiritUserLoginFormView,
                    SpiritUserLogoutView, SpiritUserRegisterFormView, activate)

app_name = "spirit_core"

urlpatterns = [
    path(
        '',
        SpiritIndexTemplateView.as_view(),
        name="index"
    ),
    path(
        'accounts/logout/',
        SpiritUserLogoutView.as_view(),
        name='logout'
    ),
    path(
        'accounts/login/',
        SpiritUserLoginFormView.as_view(),
        name='login'
    ),
    path(
        'accounts/register/',
        SpiritUserRegisterFormView.as_view(),
        name='register'
    ),
    path(
        'accounts/activate/<uidb64>/<token>/',
        activate,
        name='activate'
    ),
    
]
