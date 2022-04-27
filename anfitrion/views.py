from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, FormView


class HomeView(TemplateView):
    template_name = 'anfitrion/event.html'

class CreateEvent(FormView):
    """
    Create a new event.
    """
    pass
