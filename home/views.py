from django.views.generic import TemplateView


class Index(TemplateView):
    template_view = 'home/index.html'

