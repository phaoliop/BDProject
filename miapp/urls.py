from django.conf.urls import url

from . import views

app_name= 'miapp'
urlpatterns = [
    
    #'''
    #    VIEW
    #        -CLIENTE
    #        -PROFESION
    #        -PROFESIONALES
    #'''
    url(r'^(?P<id_cliente>[0-9]+)/view_cliente$', views.ver_cliente, name='ver_cliente'),
    url(r'^(?P<id_profesion>[0-9]+)/view_profesion$', views.ver_profesion, name='ver_profesion'),
    url(r'^(?P<dni>[0-9]+)/view_prof$', views.ver_profesional, name='ver_prof'),

    #'''
    #    SEARCH
    #        -CLIENTE = 1
    #        -PROFESION = 2
    #        -PROFESIONALES = 3
    #'''
    url(r'^ver_result$', views.ver_result, name='ver_result'),
    url(r'^ver_result2$', views.ver_result2, name='ver_result2'),
    url(r'^ver_result3$', views.ver_result3, name='ver_result3'),

    #'''
    #    FORMULARIOS
    #        -CLIENTE
    #        -PROFESION
    #        -PROFESIONALES
    #'''
    url(r'^form_cliente/$', views.form_cliente, name='form_cliente'),
    url(r'^form_profesion/$', views.form_profesion, name='form_profesion'),
    url(r'^form_profesional/$', views.form_profesional, name='form_prof'),

    #'''
    #    AGREGAR DE FORMULARIOS
    #        -CLIENTE
    #        -PROFESION
    #        -PROFESIONALES
    #'''
    url(r'^view_newdatos$', views.agregar_cliente, name='add_cliente'),
    url(r'^view_newdatos2$', views.agregar_profesion, name='add_profesion'),
    url(r'^view_newdatos3$', views.agregar_profesional, name='add_prof'),

    #'''
    #    EDITAR
    #        -CLIENTE
    #        -PROFESION
    #        -PROFESIONALES
    #'''
    url(r'^editar_cliente=(?P<id_cliente>[0-9]+)$', views.editar_cliente, name='editar_cliente'),
    url(r'^editar_profesion=(?P<id_profesion>[0-9]+)$', views.editar_profesion, name='editar_profesion'),
    url(r'^editar_prof=(?P<dni>[0-9]+)$', views.editar_profesional, name='editar_prof'),


    #'''
    #    GUARDAR CAMBIOS
    #        -CLIENTE = 1
    #        -PROFESION = 2 
    #        -PROFESIONALES = 3
    #'''
    url(r'^view_cambios$', views.guardar_cliente, name='guardar_cliente'),
    url(r'^view_cambios2$', views.guardar_profesion, name='guardar_profesion'),
    url(r'^view_cambios3$', views.guardar_profesional, name='guardar_prof'),

]