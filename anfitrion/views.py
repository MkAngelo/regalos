
import email
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AnfitrionForm, EventForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from listaDeRegalos.models import ListaDeRegalos
from .models import Evento, Anfitrion


class MenuView(LoginRequiredMixin,TemplateView):
    template_name = 'anfitrion/home.html'

@login_required
def create_view(request):
    if request.method == "POST":
        me = Anfitrion.objects.get(email=request.user.email)
        festejado_name = request.POST['festejado_first_name']
        festejado_last = request.POST['festejado_last_name']
        date = request.POST['date']
        time = request.POST['time']
        tipo = request.POST['event_type']
        lista_regalo = ListaDeRegalos.objects.filter(type=tipo)
        guests = request.POST['guests']
        direc = request.POST['address']
        card = request.POST['card']
        cvv = request.POST['cvv']

        try:
            festejado_age = int(request.POST['festejado_age'])
        except:
            return render(request, 'anfitrion/event.html', {'error': 'La edad de tu invitado es incorrecta.'})

        if festejado_age < 0 or festejado_age > 130:
            return render(request, 'anfitrion/event.html', {'error': 'La edad de tu festejado esta fuera de los limites.'})
        if guests == '':
            return render(request, 'anfitrion/event.html', {'error': 'Olvidaste poner los emails de tus invitados.'})
        if direc == '':
            return render(request, 'anfitrion/event.html', {'error': 'Olvidaste poner tu direccion, ten cuidado.'})
        if len(card) > 19 or len(card) < 19 or len(cvv) != 3:
            return render(request, 'anfitrion/event.html', {'error': 'Metodo de pago rechazado, intente con otro.'})

        evento = Evento.objects.create(
            anfitrion = me,
            festejado_first_name = festejado_name,
            festejado_last_name = festejado_last,
            festejado_age = festejado_age,
            date = date,
            time = time,
            event_type = tipo,
            card = card,
            cvv = cvv,
            address = direc,
        )
        evento.lista_regalo.set(lista_regalo)
        evento.guests = guests
        evento.save()
        return redirect('anfitrion:menu')

    return render(request, 'anfitrion/event.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('anfitrion:login')

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
