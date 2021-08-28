from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """The HomeView class displays the home page."""

    template_name = "index.html"
