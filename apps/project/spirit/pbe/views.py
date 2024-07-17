from django.views.generic import TemplateView, edit


class PBETemplateView(TemplateView):
    template_name = 'pbe_base.html'
