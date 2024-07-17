from django.views.generic import View
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'index:home'
            )
        )
        
