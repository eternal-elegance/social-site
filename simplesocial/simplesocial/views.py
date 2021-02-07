# This file contains the home page view
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "index.html"
