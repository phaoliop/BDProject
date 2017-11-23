# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-23 03:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('des_pliego', models.CharField(max_length=50)),
                ('numero_Ruc', models.CharField(max_length=12, verbose_name='Numero de Ruc')),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=400)),
                ('vigente', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corr_exp', models.CharField(max_length=4)),
                ('lugar_trabajo', models.CharField(max_length=30)),
                ('fec_inicio', models.CharField(max_length=20)),
                ('fec_fin', models.CharField(max_length=20)),
                ('des_trabajo', models.CharField(max_length=500)),
                ('motivo_retirno', models.CharField(max_length=30)),
                ('cargo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Fase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desFase', models.TextField(max_length=200, verbose_name='Descripcion Fase')),
                ('vigente', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('dni', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('apellidoPaterno', models.CharField(max_length=50)),
                ('apellidoMaterno', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=9)),
                ('coreo', models.CharField(max_length=100)),
                ('cod_dist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Distrito')),
                ('cod_dpto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Persona_TICS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('de_medio', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PersonaProf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Universidad', models.CharField(max_length=50)),
                ('Vigente', models.CharField(max_length=20)),
                ('dni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Persona')),
            ],
        ),
        migrations.CreateModel(
            name='Profesion',
            fields=[
                ('id_profesion', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('Grado', models.CharField(max_length=50)),
                ('Des_profesion', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Departamento', verbose_name='Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codSnip', models.CharField(max_length=10, verbose_name='Codigo.Pres.Asociado')),
                ('nombre', models.CharField(max_length=100)),
                ('fechReg', models.DateField(verbose_name='Fecha Registro')),
                ('funcion', models.CharField(max_length=100)),
                ('observacion', models.TextField(max_length=500)),
                ('vigente', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=2)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Cliente', verbose_name='Cliente')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Departamento')),
                ('distrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Distrito')),
                ('especialista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='espe', to='project.Persona', verbose_name='Especialista')),
                ('fase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Fase')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Provincia')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Persona', verbose_name='Responsable Proy.')),
            ],
        ),
        migrations.CreateModel(
            name='ProyectoCosto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costoPip', models.FloatField(verbose_name='Costo proyecto.Inv.Publica')),
                ('costoEquipo', models.FloatField(verbose_name='Costo Equipo')),
                ('costoAdm', models.FloatField(verbose_name='Costo Administracion')),
                ('costoImp', models.FloatField(verbose_name='Costo Implementacion')),
                ('costoOtros', models.FloatField(verbose_name='Costo Otros')),
                ('observacion', models.TextField(max_length=500)),
                ('vigente', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=2)),
                ('fase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Fase')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='ProyectoDocs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoNivel', models.IntegerField()),
                ('fechInicio', models.DateField(verbose_name='Fecha Inicio')),
                ('fechFin', models.DateField(verbose_name='Fecha Final')),
                ('media', models.FileField(blank=True, null=True, upload_to='myfolder/')),
                ('observacion', models.TextField(max_length=500)),
                ('tipoEntregable', models.IntegerField()),
                ('codEntrega', models.IntegerField()),
                ('vigente', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=2)),
                ('especialista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='especial', to='project.Persona', verbose_name='Especialista')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Estado')),
                ('fase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Fase')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Proyecto')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Persona', verbose_name='Responsable Doc.')),
            ],
        ),
        migrations.CreateModel(
            name='TICS',
            fields=[
                ('id_TICS', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('des_TICS', models.CharField(max_length=20)),
                ('vigente', models.CharField(max_length=4)),
            ],
        ),
        migrations.AddField(
            model_name='personaprof',
            name='id_profesional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Profesion'),
        ),
        migrations.AddField(
            model_name='persona_tics',
            name='id_TICS',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.TICS'),
        ),
        migrations.AddField(
            model_name='persona_tics',
            name='id_persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Persona'),
        ),
        migrations.AddField(
            model_name='persona',
            name='cod_prov',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Provincia'),
        ),
        migrations.AddField(
            model_name='experiencia',
            name='id_persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Persona'),
        ),
        migrations.AddField(
            model_name='experiencia',
            name='id_profesional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Profesion'),
        ),
        migrations.AddField(
            model_name='estado',
            name='fase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Fase'),
        ),
        migrations.AddField(
            model_name='estado',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Proyecto'),
        ),
        migrations.AddField(
            model_name='distrito',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Provincia', verbose_name='Provincia'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Departamento', verbose_name='Departamento'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='distrito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Distrito', verbose_name='Distrito'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='ger_Infraestructura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Persona', verbose_name='Gerente Ifraestructura'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='per_General',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='general', to='project.Persona', verbose_name='Gerente General'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Provincia', verbose_name='Provincia'),
        ),
    ]
