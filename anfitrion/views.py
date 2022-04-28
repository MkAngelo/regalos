
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AnfitrionForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


class MenuView(LoginRequiredMixin,TemplateView):
    template_name = 'anfitrion/event.html'

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('anfitrion:menu')
        else: 
            return render(request, 'anfitrion/login.html', {'error': 'usuario o password invalido'})
    return render(request, 'anfitrion/login.html')    

class SignUpView(FormView):
    """
    Create a new anfitrion user.
    """
    template_name = 'anfitrion/signup.html'
    form_class = AnfitrionForm
    success_url = reverse_lazy('anfitrion:login')

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context.update({'error': 'revisa que tus datos sean correctos.'})
        return self.render_to_response(context)

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
