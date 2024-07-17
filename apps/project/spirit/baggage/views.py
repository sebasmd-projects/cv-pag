from django.views.generic import TemplateView, edit


class BaggageTemplateView(TemplateView):
    template_name = 'baggage_base.html'
