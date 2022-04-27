
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView, FormView
from .forms import AnfitrionForm


class MenuView(TemplateView):
    template_name = 'anfitrion/event.html'

class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'anfitrion/login.html'

class SignUpView(FormView):
    """
    Create a new anfitrion user.
    """
    template_name = 'anfitrion/signup.html'
    form_class = AnfitrionForm
    success_url = reverse_lazy('anfitrion:login')

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
