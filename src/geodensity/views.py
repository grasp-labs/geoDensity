from django.views.generic import TemplateView


class IndexView(TemplateView):
    """
    Homepage for AiderPrime
    """
    template_name = 'geodensity/index.html'
