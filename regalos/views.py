# Django
from multiprocessing import context
from django.views.generic import TemplateView, DetailView
from django.shortcuts import redirect, render

# Models
from anfitrion.models import Evento
from listaDeRegalos.models import ListaDeRegalos

# Forms
from .forms import MetodoDePagoForm


class InicioView(TemplateView):
    template_name = 'regalos/index.html'

class InvitadoView(DetailView):
    template_name = 'regalos/invitado.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    queryset = Evento.objects.all()

class CompraView(DetailView):
    template_name = 'regalos/compra.html'
    model = ListaDeRegalos
    pk_url_kwarg = 'type'

    def get_queryset(self):
        e = Evento.objects.get(id=self.kwargs['event_id'],)

        return ListaDeRegalos.objects.filter(type=e.event_type)

def compra_view(request, event_id, event_type):
    lista_regalo = ListaDeRegalos.objects.filter(type=event_type)
    context = {'regalos': lista_regalo, 'event_k': event_id}
    return render(request, 'regalos/compra.html', context)

def pagar_view(request, event_id, event_type, regalo_id):
    regalo = ListaDeRegalos.objects.get(pk=regalo_id)
    context = {'regalo': regalo, 'event_type': event_type, 'event_id': event_id}
    if request.method == 'POST':
        form = MetodoDePagoForm(request.POST)
        if form.is_valid():
            evento = Evento.objects.get(id=event_id)
            evento.total = evento.total + 1
            evento.save()
            return redirect('completado')
        else:
            context = {'regalo': regalo, 'event_type': event_type, 'event_id': event_id, 'form':form}
            return render(request, 'regalos/pagar.html',context)
    return render(request, 'regalos/pagar.html', context)

def completado_view(request):
    return render(request, 'regalos/completado.html')