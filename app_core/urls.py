from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from django.utils.translation import gettext_lazy as _
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from apps.project.page.index.sitemaps import IndexViewSitemap

schema_view = get_schema_view(
    openapi.Info(
        title='Backend Endpoints',
        default_version='v1.0.0',
        description=_('API documentation and endpoint representation'),
        terms_of_service='',
        contact=openapi.Contact(email=settings.YASG_DEFAULT_EMAIL),
        license=openapi.License(name=settings.YASG_TERMS_OF_SERVICE),
    ),
    public=False,
)

admin_url = settings.ADMIN_URL

custom_apps = settings.CUSTOM_APPS
spirit_apps = settings.SPIRIT_APPS

utils_path = settings.UTILS_PATH

apps_urls = [path('', include(f'{app}.urls')) for app in custom_apps]
apps_urls += [path('spirit/', include(f'{app}.urls')) for app in spirit_apps]

apps_sitemaps = {
    'home': IndexViewSitemap
}

handler400 = f'{utils_path}.views.handler400'

handler403 = f'{utils_path}.views.handler403'

handler404 = f'{utils_path}.views.handler404'

handler500 = f'{utils_path}.views.handler500'

admin_urls = [
    path(admin_url, admin.site.urls),
]

sitemap_urls = [
    re_path(
        r"^sitemap.xml",
        sitemap,
        {
            'sitemaps': apps_sitemaps
        },
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

account_urls = [
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(),
        name='login'
    ),
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
]

swagger_urls = [
    re_path(
        r'^api/docs/',
        schema_view.with_ui(
            'swagger',
            cache_timeout=0
        ),
        name='schema-swagger-ui'
    ),
    re_path(
        r'^api/redocs/',
        schema_view.with_ui(
            'redoc',
            cache_timeout=0
        ),
        name='schema-redoc'
    ),
    re_path(
        r'^api/docs/<format>/',
        schema_view.without_ui(
            cache_timeout=0
        ),
        name='schema-json-yaml'
    ),
]

ckeditor_urls = [
    path(
        "ckeditor5/",
        include('django_ckeditor_5.urls')
    ),
]

roseta_urls = [
    re_path(
        r'^rosetta/',
        include('rosetta.urls')
    ),
]

urlpatterns = admin_urls + account_urls + ckeditor_urls
urlpatterns += apps_urls + sitemap_urls + swagger_urls + roseta_urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
