
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
import datetime

# Create your models here.

#Clases del sistema

#persona
class Persona(models.Model):
	#id_persona =  models.CharField(max_length=8, primary_key=True)
	#dni = models.CharField(max_length=8)
	tip_persona = models.CharField(max_length=1)
	des_persona = models.CharField(max_length=100)
	des_corta = models.CharField(max_length=30)
	flag_cli = models.CharField(max_length=1)
	flag_esp = models.CharField(max_length=1)
	flag_prof = models.CharField(max_length=1)
	direccion = models.CharField(max_length=100)
	hobby = models.CharField(max_length=1000) #falta foto
	fec_nac = models.CharField(max_length=20)
	cod_dpto = models.CharField(max_length=8)
	cod_prov = models.CharField(max_length=8)
	cod_dist = models.CharField(max_length=8)
	nro_CIP = models.CharField(max_length=10)
	fec_CIP_Vig = models.CharField(max_length=20)
	centro_trabajo = models.CharField(max_length=10)
	cargo = models.CharField(max_length=20)
	lic_cond = models.CharField(max_length=4)
	obs = models.CharField(max_length=300)

	def __str__(self):	
		return self.id_persona



#######################

