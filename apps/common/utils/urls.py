from django.urls import include, re_path, path

from .api import urls as api_urls
from .views import robots_txt, set_language


urlpatterns = [
    path('robots.txt', robots_txt),
    path('set_language/', set_language, name='set_language'),
    re_path(r'^api/logs/v1/', include(api_urls.log_urlpattern)),
    re_path(r'^api/auth/v1/', include(api_urls.urlpatterns)),
]
