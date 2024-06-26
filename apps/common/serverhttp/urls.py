from django.urls import path, re_path
from .views import HttpRequestAttakView

app_name = 'serverhttp'

urlpatterns = [
    path(
        '*',
        HttpRequestAttakView.as_view(),
        name='httprequest'
    ),
    re_path(
        r'^.*[Ss][Ee][Tt][Uu][Pp].*',
        HttpRequestAttakView.as_view(),
        name="setup"
    ),
    re_path(
        r'^.*[Ee][Nn][Vv].*',
        HttpRequestAttakView.as_view(),
        name="env"
    ),
    re_path(
        r'^.*[Pp][Hh][Pp][Mm][Yy][Aa][Dd][Mm][Ii][Nn].*',
        HttpRequestAttakView.as_view(),
        name="phpmyadmin"
    ),
    re_path(
        r'^.*[Ww][Ee][Pp][Mm][Yy][Aa][Dd][Mm][Ii][Nn].*',
        HttpRequestAttakView.as_view(),
        name="wepmyadmin"
    ),
    re_path(
        r'^.*[Hh][Tt][Mm][Ll].*',
        HttpRequestAttakView.as_view(),
        name="html"
    ),
    re_path(
        r'^.*[Tt][Xx][Tt].*',
        HttpRequestAttakView.as_view(),
        name="txt"
    ),
    re_path(
        r'^.*[Ww][Ee][Ll][Ll]-?[Kk][Nn][Oo][Ww][Nn].*',
        HttpRequestAttakView.as_view(),
        name="well-known"
    ),
    re_path(
        r'^.*[Pp][Hh][Pp].*',
        HttpRequestAttakView.as_view(),
        name="php"
    ),
]
