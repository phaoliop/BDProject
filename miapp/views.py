# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from project.models import Cliente, Profesion, PersonaProf, Persona, Departamento, Provincia, Distrito

'''
	EDITAR-GUARDAR
		-CLIENTE
		-PROFESION
		-PROFESIONAL
'''
##Editar Cliente
def editar_cliente(request, id_cliente):
	cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
	return render(request, 'miapp/editar_cliente.html', {'cliente':cliente})
	pass
def guardar_cliente(request):
	id_cliente = request.POST['id_cliente']

	if id_cliente:
		try:
			var = ""
			cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
			id_cliente = request.POST['id_cliente']
			departamento = request.POST['departamento']
			provincia = request.POST['provincia']
			distrito = request.POST['distrito']
			per_General = request.POST['per_General']
			ger_Infraestructura = request.POST['ger_Infraestructura']

			cliente.id_cliente = request.POST['id_cliente']
			cliente.des_pliego = request.POST['des_pliego']
			cliente.departamento = Departamento.objects.get(nombre=departamento)
			cliente.provincia = Provincia.objects.get(nombre=provincia)
			cliente.distrito = Distrito.objects.get(nombre=distrito)
			cliente.numero_Ruc = request.POST['numero_Ruc']
			cliente.per_General = Persona.objects.get(pk=per_General)
			cliente.ger_Infraestructura = Persona.objects.get(pk=ger_Infraestructura)
			cliente.save()
			pass
			return render(request, 'miapp/ver_cliente.html',{'cliente':  cliente, 'message_add': 'Sus cambios han sido guardados!'})
		except var:
			return render(request, 'miapp/editar_cliente.html', {'error_message': var})
	else:
		return render(request, 'miapp/editar_cliente.html')
	pass

##Editar Profesion
def editar_profesion(request, id_profesion):
	profesion = get_object_or_404(Profesion, id_profesion=id_profesion)
	return render(request, 'miapp/editar_profesion.html', {'prof':profesion})
	pass
def guardar_profesion(request):
	id_profesion = request.POST['id_profesion']

	if id_profesion:
		try:
			profesion = get_object_or_404(Profesion, id_profesion=id_profesion)

			profesion.id_profesion = request.POST['id_profesion']
			profesion.Des_profesion = request.POST['des_profesion']
			profesion.Grado = request.POST['Grado']
			profesion.save()
			pass
			return render(request, 'miapp/ver_profesion.html',{'prof':  profesion, 'message_add': 'Sus cambios han sido guardados!'})
		except:
			return render(request, 'miapp/editar_profesion.html', {'error_message': 'Datos no se han podido guardar!'})
	else:
		return render(request, 'miapp/editar_profesion.html')
	pass

##Editar Profesional
def editar_profesional(request, dni):
	profesional = get_object_or_404(PersonaProf, dni=dni)
	return render(request, 'miapp/editar_profesional.html', {'prof':profesional})
	pass
def guardar_profesional(request):
	dni = request.POST['dni']
	id_profesional = request.POST['id_profesional']

	if dni and id_profesional:
		var = ""
		try:
			profesional = get_object_or_404(PersonaProf, dni=dni)
			profesional.dni = Persona.objects.get(pk=dni)
			profesional.id_profesional = Profesion.objects.get(pk=id_profesional)
			profesional.Universidad = request.POST['Universidad']
			profesional.Vigente = request.POST['Vigente']

			profesional.save()
			pass
			return render(request, 'miapp/ver_profesional.html',{'prof':  profesional, 'message_add': 'Sus cambios han sido guardados!'})
		except var:
			return render(request, 'miapp/editar_profesional.html', {'error_message': 'Ingrese datos existentes.'})
	else:
		return render(request, 'miapp/editar_profesional.html')
	pass
'''
	FORMULARIOS-AGREGAR
		-CLIENTE
		-PROFESION
		-PROFESIONAL
'''
##Formulario Cliente
def form_cliente(request):
	lista_departamentos = Departamento.objects.order_by('pk')
	lista_personas = Persona.objects.order_by('pk')
	return render(request, 'miapp/form_cliente.html',{'lista_departamentos':lista_departamentos, 'lista_personas':lista_personas})
	pass
def agregar_cliente(request):
	var = ""
	try:
		id_cliente = request.POST['id_cliente']
		departamento = request.POST['departamento']
		provincia = request.POST['provincia']
		distrito = request.POST['distrito']
		per_General = request.POST['per_General']
		ger_Infraestructura = request.POST['ger_Infraestructura']

		client = Cliente(
		id_cliente = request.POST['id_cliente'],
		des_pliego = request.POST['des_pliego'],
		departamento = Departamento.objects.get(pk=departamento),
		provincia = Provincia.objects.get(nombre=provincia),
		distrito = Distrito.objects.get(nombre=distrito),
		numero_Ruc = request.POST['numero_Ruc'],
		per_General = Persona.objects.get(pk=per_General),
		ger_Infraestructura = Persona.objects.get(pk=ger_Infraestructura),
		)
		client.save()
		return render(request, 'miapp/ver_cliente.html',{'cliente':  client,'message_add': 'Nuevo cliente agregado!'})
	except var:
		return render(request, 'miapp/form_cliente.html', {'error_message': 'Nuevo cliente no agregado!' } )
	pass

##Formulario Profesion	
def form_profesion(request):
	return render(request, 'miapp/form_profesion.html')
	pass
def agregar_profesion(request):
	try:
		profesion = Profesion(
		id_profesion = request.POST['id_profesion'],
		Des_profesion = request.POST['des_profesion'],
		Grado = request.POST['grado'],
		)
		profesion.save()
		return render(request, 'miapp/ver_profesion.html',{'prof':  profesion, 'message_add': 'Agregado con exito!'})
	except:
		return render(request, 'miapp/form_profesion.html', {'error_message': 'Nueva profesion no agregada!'})
	pass

##Formulario Profesional
def form_profesional(request):
	lista_profesiones = Profesion.objects.order_by('pk')
	lista_personas = Persona.objects.order_by('pk')
	return render(request, 'miapp/form_profesional.html',{'lista_profesiones': lista_profesiones, 'lista_personas':lista_personas})
	pass
def agregar_profesional(request):
	lista_profesiones = PersonaProf.objects.order_by('-pk')
	var = ""
	try:
		dni = request.POST['dni']
		id_profesional = request.POST['id_profesional']

		profesional = PersonaProf(
		dni = Persona.objects.get(pk=dni),
		id_profesional = Profesion.objects.get(pk=id_profesional),
		Universidad = request.POST['Universidad'],
		Vigente = request.POST['Vigente'],
		)
		profesional.save()
		return render(request, 'miapp/ver_profesional.html',{'prof':  profesional,'lista_profesiones': lista_profesiones ,'message_add': 'Agregado con exito!'})
	except var:
		return render(request, 'miapp/form_profesional.html', {'error_message': var})
	pass

'''
	VISTAS-BUSQUEDAS
		-CLIENTE
		-PROFESION
		-PROFESIONAL
'''
	
###Ver cliente
def ver_cliente(request, id_cliente):
	if id_cliente!='0':
		cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
		pass
		return render(request, 'miapp/ver_cliente.html', {'cliente': cliente})
	else:
		return render(request, 'miapp/ver_cliente.html', {'cliente': None})

def ver_result(request):
	id_cliente = request.GET['cliente']
	var = ""
	try:
		cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
		return render(request, 'miapp/ver_cliente.html', {'cliente': cliente})
	except var:
		return render(request, 'miapp/ver_cliente.html', {'cliente': None, 'error_message': var})
	pass

###Ver profesion
def ver_profesion(request, id_profesion):
	if id_profesion!='0':
		profesion = get_object_or_404(Profesion, id_profesion=id_profesion)
		pass
		return render(request, 'miapp/ver_profesion.html', {'prof': profesion})
	else:
		return render(request, 'miapp/ver_profesion.html', {'prof': None})

def ver_result2(request):
	id_profesion = request.GET['profesion']

	try:
		profesion = get_object_or_404(Profesion, id_profesion=id_profesion)
		return render(request, 'miapp/ver_profesion.html', {'prof': profesion})
	except:
		return render(request, 'miapp/ver_profesion.html', {'prof': None, 'error_message': 'Id no encontrado!'})
	pass

###Ver profesional
def ver_profesional(request, dni):
	if dni!='0':
		profesional = get_object_or_404(PersonaProf, dni=dni)
		pass
		return render(request, 'miapp/ver_profesional.html', {'prof': profesional})
	else:
		return render(request, 'miapp/ver_profesional.html', {'prof': None})

def ver_result3(request):
	dni_profesional = request.GET['dni']
	
	try:
		profesional = get_object_or_404(PersonaProf, dni=dni_profesional)
		return render(request, 'miapp/ver_profesional.html', {'prof': profesional})
	except:
		return render(request, 'miapp/ver_profesional.html', {'prof':  None, 'error_message': 'Id no encontrado!'})
	pass
