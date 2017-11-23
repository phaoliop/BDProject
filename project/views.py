# -*- coding: utf-8 -*-
from __future__ import unicode_literals
 

from django.http import HttpResponse


from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (

    CreateView,
    UpdateView,
    DeleteView
)

from .models import Proyecto
from .models import ProyectoDocs
from .models import ProyectoCosto
from .models import Cliente, Profesion, PersonaProf, Persona


##PROYECTO
def index(request):
    lista_personas = Persona.objects.order_by('-pk')[:5]
    lista_profesiones = Profesion.objects.order_by('pk')
    lista_clientes = Cliente.objects.order_by('-pk')[:10]
    lista_proyectos = Proyecto.objects.order_by('pk')[:5]

    context = { 'lista_personas': lista_personas, 'lista_profesiones': lista_profesiones, 'lista_clientes': lista_clientes, 'lista_proyectos':lista_proyectos}
    return render(request, 'project/index.html', context)
    pass

class ProyectoList(ListView):
    model = Proyecto
    template_name = 'project/lista_proyecto.html'


def ProyectoListFunc(request):
    proyectos = Proyecto
    return render(request,'project/lista_proyecto.html', {'proyectos': proyectos})


class ProyectoCreacion(CreateView):
    model = Proyecto
    success_url = reverse_lazy('project:list_p')
    fields = ['fase','codSnip','nombre','fechReg','funcion','departamento','distrito','provincia','cliente','especialista','responsable','observacion','vigente']
    template_name = 'project/registro_proyecto.html'


class ProyectoUpdate(UpdateView):
    model = Proyecto
    success_url = reverse_lazy('project:list_p')
    fields = ['fase','codSnip','nombre','fechReg','funcion','departamento','distrito','provincia','cliente','especialista','responsable','observacion','vigente']
    template_name='project/update_proyecto.html'


class ProyectoDetail(DetailView):
    model = Proyecto
    template_name='project/detalle_proyecto.html'


class ProyectoDelete(DeleteView):
    model = Proyecto
    success_url = reverse_lazy('project:list_p')
    template_name='project/delete_proyecto.html'


##ProyetcoDocs

class ProyectoListDocs(ListView):
    model = ProyectoDocs
    template_name = 'project/lista_proyectodocs.html'

class ProyectoDocsCreacion(CreateView):
    model = ProyectoDocs
    success_url = reverse_lazy('project:list_pd')
    fields = ['proyecto','fase','codigoNivel','fechInicio','fechFin','media','observacion','estado','tipoEntregable','codEntrega','especialista','responsable','vigente']
    template_name = 'project/registro_proyectodocs.html'

class ProyectoDocsUpdate(UpdateView):
    model = ProyectoDocs
    success_url = reverse_lazy('project:list_pd')
    fields = ['proyecto','fase','codigoNivel','fechInicio','fechFin','media','observacion','estado','tipoEntregable','codEntrega','especialista','responsable','vigente']
    template_name='project/update_proyectodocs.html'


class ProyectoDocsDetail(DetailView):
    model = ProyectoDocs
    template_name='project/detalle_proyectodocs.html'


class ProyectoDocsDelete(DeleteView):
    model = ProyectoDocs
    success_url = reverse_lazy('project:list_pd')
    template_name='project/delete_proyectodocs.html'


##Proyecto costo

class ProyectoCostoList(ListView):
    model = ProyectoCosto
    template_name = 'project/lista_proyectocosto.html'


class ProyectoCostoCreacion(CreateView):
    model = ProyectoCosto
    success_url = reverse_lazy('project:list_pc')
    fields = ['proyecto','costoPip','costoEquipo','costoAdm','costoAdm','costoImp','costoOtros','fase','observacion','vigente']
    template_name = 'project/registro_proyectocosto.html'


class ProyectoCostoUpdate(UpdateView):
    model = ProyectoCosto
    success_url = reverse_lazy('project:list_pc')
    fields = ['proyecto','costoPip','costoEquipo','costoAdm','costoAdm','costoImp','costoOtros','fase','observacion','vigente']
    template_name='project/update_proyectocosto.html'


class ProyectoCostoDetail(DetailView):
    model = ProyectoCosto
    template_name='project/detalle_proyectocosto.html'


class ProyectoCostoDelete(DeleteView):
    model = ProyectoCosto
    success_url = reverse_lazy('project:list_pc')
    template_name='project/delete_proyectocosto.html'