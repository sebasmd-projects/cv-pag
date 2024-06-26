from django.shortcuts import render

from django.views.generic import TemplateView

class IndexTemplateView(TemplateView):
    template_name = 'project/page/index/templates/page/index.html'

