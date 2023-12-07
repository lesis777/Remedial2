from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import *
from django.views import generic

class JugadorDetailView(DetailView):
    model = Jugador
    template_name = 'nfl_app/detalle_jugador.html'


class JugadorUpdateView(UpdateView):
    model = Jugador
    template_name = 'nfl_app/jugador_form.html'
    fields = ['nombre', 'posicion', 'numero', 'equipo']


class JugadorDeleteView(DeleteView):
    model = Jugador
    template_name = 'nfl_app/jugador_confirm_delete.html'
    success_url = reverse_lazy('lista_jugadores')


class JugadorCreateView(CreateView):
    model = Jugador
    template_name = 'nfl_app/jugador_form.html'
    fields = ['nombre', 'posicion', 'numero', 'equipo']


class EquipoDetailView(DetailView):
    model = Equipo
    template_name = 'nfl_app/detalle_equipo.html'


class EquipoUpdateView(UpdateView):
    model = Equipo
    template_name = 'nfl_app/equipo_form.html'
    fields = ['nombre', 'Propietario', 'estadio']


class EquipoDeleteView(DeleteView):
    model = Equipo
    template_name = 'nfl_app/equipo_confirm_delete.html'
    success_url = reverse_lazy('lista_equipos')


class EquipoCreateView(CreateView):
    model = Equipo
    template_name = 'nfl_app/equipo_form.html'
    fields = ['nombre', 'dueño', 'estadio']


class EventoDetailView(DetailView):
    model = Evento
    template_name = 'nfl_app/detalle_evento.html'


class EventoUpdateView(UpdateView):
    model = Evento
    template_name = 'nfl_app/evento_form.html'
    fields = ['nombre', 'equipo']


class EventoDeleteView(DeleteView):
    model = Evento
    template_name = 'nfl_app/evento_confirm_delete.html'
    success_url = reverse_lazy('lista_eventos')

# Vista para crear un evento
class EventoCreateView(CreateView):
    model = Evento
    template_name = 'nfl_app/evento_form.html'
    fields = ['nombre', 'equipo']

# Vista para ver detalles de un estadio
class EstadioDetailView(DetailView):
    model = Estadio
    template_name = 'nfl_app/detalle_estadio.html'

# Vista para actualizar un estadio
class EstadioUpdateView(UpdateView):
    model = Estadio
    template_name = 'nfl_app/estadio_form.html'
    fields = ['nombre', 'capacidad', 'tamaño']

# Vista para eliminar un estadio
class EstadioDeleteView(DeleteView):
    model = Estadio
    template_name = 'nfl_app/estadio_confirm_delete.html'
    success_url = reverse_lazy('lista_estadios')

# Vista para crear un estadio
class EstadioCreateView(CreateView):
    model = Estadio
    template_name = 'nfl_app/estadio_form.html'
    fields = ['nombre', 'capacidad', 'tamaño']

# Vista para ver detalles de un propietario
class PropietarioDetailView(DetailView):
    model = Propietario
    template_name = 'nfl_app/detalle_propietario.html'

# Vista para actualizar un propietario
class PropietarioUpdateView(UpdateView):
    model = Propietario
    template_name = 'nfl_app/propietario_form.html'
    fields = ['nombre', 'edad', 'equipo']


class PropietarioDeleteView(DeleteView):
    model = Propietario
    template_name = 'nfl_app/propietario_confirm_delete.html'
    success_url = reverse_lazy('lista_propietarios')


class PropietarioCreateView(CreateView):
    model = Propietario
    template_name = 'nfl_app/propietario_form.html'
    fields = ['nombre', 'edad', 'equipo']

class IndexView(generic.View):
    template_name = 'home/index.html' 
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

