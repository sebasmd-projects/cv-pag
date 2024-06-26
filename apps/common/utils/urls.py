from django.urls import include, re_path, path

from .api import urls as api_urls
from .views import robots_txt


urlpatterns = [
    path('robots.txt', robots_txt),
    re_path(r'^api/logs/v1/', include(api_urls.log_urlpattern)),
    re_path(r'^api/auth/v1/', include(api_urls.urlpatterns)),
]
