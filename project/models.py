# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Departamento(models.Model):
	nombre = models.CharField(max_length=100,verbose_name="Nombre")
	def __str__(self):
	    return self.nombre


class Provincia(models.Model):
	departamento = models.ForeignKey(Departamento,verbose_name="Departamento", on_delete=models.CASCADE)
	nombre = models.CharField(max_length=100,verbose_name="Nombre")
	def __str__(self):
		return self.nombre

class Distrito(models.Model):
	provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE,verbose_name="Provincia")
	nombre = models.CharField(max_length=100,verbose_name="Nombre")
	def __str__(self):
		return self.nombre

class Persona(models.Model):
    dni=models.CharField(max_length=8, primary_key=True)
    Nombre=models.CharField(max_length=50)
    apellidoPaterno=models.CharField(max_length=50)
    apellidoMaterno=models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    cod_dpto = models.ForeignKey(Departamento)
    cod_prov = models.ForeignKey(Provincia)
    cod_dist = models.ForeignKey(Distrito)
    telefono=models.CharField(max_length=9)
    coreo=models.CharField(max_length=100)

    def __str__(self):
		return self.dni

class Profesion(models.Model):
    id_profesion = models.CharField(max_length=32, primary_key=True)
    Grado = models.CharField(max_length=50)
    Des_profesion = models.TextField(max_length=50)

    def __str__(self):
		return self.id_profesion

class PersonaProf(models.Model):
    dni = models.ForeignKey(Persona)
    id_profesional = models.ForeignKey(Profesion)
    Universidad = models.CharField(max_length=50)
    Vigente = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.dni)

class Cliente(models.Model):
    id_cliente = models.CharField(max_length=8, primary_key = True)
    des_pliego = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE,verbose_name="Departamento")
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE,verbose_name="Provincia")
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE,verbose_name="Distrito")
    numero_Ruc =  models.CharField(max_length=12,verbose_name="Numero de Ruc")
    per_General = models.ForeignKey(Persona, on_delete=models.CASCADE,verbose_name="Gerente General",related_name="general")
    ger_Infraestructura = models.ForeignKey(Persona, on_delete=models.CASCADE,verbose_name="Gerente Ifraestructura")
    def __str__(self):
        return self.numero_Ruc

class Fase(models.Model):

    SI = 'Si'
    NO = 'No'

    VIGENCIA_CHOICES = (
        (SI, 'Si'),
        (NO, 'No'),
    )

    desFase = models.TextField(max_length=200, verbose_name="Descripcion Fase")
    vigente = models.CharField(max_length=2,choices=VIGENCIA_CHOICES)
    def __str__(self):
        return self.desFase

class Proyecto(models.Model):

    SI = 'Si'
    NO = 'No'

    VIGENCIA_CHOICES = (
        (SI, 'Si'),
        (NO, 'No'),
    )


    fase = models.ForeignKey(Fase, on_delete=models.CASCADE)  
    codSnip = models.CharField(max_length=10,verbose_name='Codigo.Pres.Asociado')
    nombre= models.CharField(max_length=100)
    fechReg = models.DateField(verbose_name='Fecha Registro')      
    funcion = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,verbose_name='Cliente')
    especialista = models.ForeignKey(Persona, on_delete=models.CASCADE,verbose_name="Especialista",related_name="espe")
    responsable = models.ForeignKey(Persona, on_delete=models.CASCADE,verbose_name="Responsable Proy.")
    observacion = models.TextField(max_length=500)
    vigente = models.CharField(max_length=2,choices=VIGENCIA_CHOICES)

    def __str__(self):
        return self.nombre

class Estado(models.Model):

    SI = 'Si'
    NO = 'No'

    VIGENCIA_CHOICES = (
        (SI, 'Si'),
        (NO, 'No'),
    )

    fase = models.ForeignKey(Fase, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=400)
    vigente = models.CharField(max_length=2,choices=VIGENCIA_CHOICES)


class ProyectoDocs(models.Model):

    SI = 'Si'
    NO = 'No'

    VIGENCIA_CHOICES = (
        (SI, 'Si'),
        (NO, 'No'),
    )

    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE)
    codigoNivel = models.IntegerField()
    fechInicio =models.DateField(verbose_name='Fecha Inicio')  
    fechFin = models.DateField(verbose_name='Fecha Final')    
    media = models.FileField(upload_to='myfolder/',blank=True,null=True)
    observacion = models.TextField(max_length=500)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    tipoEntregable = models.IntegerField()
    codEntrega = models.IntegerField()
    especialista = models.ForeignKey(Persona, on_delete=models.CASCADE,verbose_name="Especialista",related_name="especial")
    responsable = models.ForeignKey(Persona, on_delete=models.CASCADE,verbose_name="Responsable Doc.")
    vigente = models.CharField(max_length=2,choices=VIGENCIA_CHOICES)
    

class ProyectoCosto(models.Model):

    SI = 'Si'
    NO = 'No'

    VIGENCIA_CHOICES = (
        (SI, 'Si'),
        (NO, 'No'),
    )

    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    costoPip = models.FloatField(verbose_name='Costo proyecto.Inv.Publica')
    costoEquipo = models.FloatField(verbose_name='Costo Equipo')
    costoAdm = models.FloatField(verbose_name='Costo Administracion')
    costoImp = models.FloatField(verbose_name='Costo Implementacion')
    costoOtros = models.FloatField(verbose_name='Costo Otros')
    fase = models.ForeignKey(Fase, on_delete=models.CASCADE)
    observacion = models.TextField(max_length=500) 
    vigente = models.CharField(max_length=2,choices=VIGENCIA_CHOICES)

#experiencia
class Experiencia(models.Model):
    id_persona =  models.ForeignKey(Persona)
    corr_exp = models.CharField(max_length=4)
    lugar_trabajo = models.CharField(max_length=30)
    fec_inicio = models.CharField(max_length=20)
    fec_fin = models.CharField(max_length=20)
    des_trabajo = models.CharField(max_length=500)
    motivo_retirno = models.CharField(max_length=30)
    cargo = models.CharField(max_length=20)
    id_profesional = models.ForeignKey(Profesion)

    def __str__(self):  
        return self.corr_exp

#tics
class TICS(models.Model):
    id_TICS = models.CharField(max_length=8, primary_key=True)
    des_TICS = models.CharField(max_length=20)
    vigente = models.CharField(max_length=4)
    def __str__(self):  
        return self.id_TICS

#persona tics
class Persona_TICS(models.Model):
    id_persona =  models.ForeignKey(Persona)
    id_TICS = models.ForeignKey(TICS)
    de_medio = models.CharField(max_length=100)

    def __str__(self):  
        return self.id_TICS