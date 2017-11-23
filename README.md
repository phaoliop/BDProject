# Datosnow
### Django+Mysql+Firebase

### Info

Aplicación web hecha en Django y Mysql, ademas por agregar el uso de Firebase para obtener algunos datos de la nube. Permite realizar las funcionalidades basicas (Agregar, Buscar, Visualizar, Editar) relacionadas con nuestras clases:
  * Clientes
  * Profesiones
  * Profesionales

### Modelo de Base de Datos
![Imagen no disponible](https://github.com/phaoliop/Datosnow/blob/master/imagenes/bd_basic.png)

### HERRAMIENTAS:
 * Django
   * Version: 1.11.5
   
 * Virtualenv
   * Version: 15.1.0
   
 * pip
   * Version: 9.0.1
  
 * Sublime Text Build 3126

### Dependencias  
* Python
  * Version: 2.7.6
  
* python-firebase
  * Version: 1.2
  
* requests
  * Version: 2.18.4
  
* MySQL-python
  * Version: 1.2.5 

### Ejecucion
Tener instalado pip y virtualenv, Mysql:

Una vez instalado, crear una Base de datos llamada Datosnow_data:
* $ mysql -u usuario -p
 * Ingresan su clave
* > create database Datosnow_data;
 * Nota: en todo caso modificar el archivo my.cnf y cambiar los datos de la conexion y la base de datos.
 
Luego darle permisos al archivo install.sh :
* $ sudo chmod 777 install.sh 
Nos ubicamos dentro de la carpeta y ejecutamos el script de instalacion:
* $ ./install.sh

 * Nota: El script inicia el servidor por defecto en la direccion 127.0.0.1:8000

Para iniciar otra vez, se ubican en la ubicacion donde se encuentra el proyecto y ejecutan:
* $ source kernel/bin/activate
* $ python manage.py runserver


### INTEGRANTES:
 * RAMIREZ GIRON, PAOLO AXEL
 * TORRES HUAROMA, ALEJANDRO
 * RIVARA OXA, GENARO JUNIOR
 * VENTURA VALENCIA, RAUL
 * ALFARO SALINAS, ELMER
 
 
### Prueba Web:
#### Prueba-1:
![Prueba-1 no disponible](https://github.com/phaoliop/BDProject/blob/master/imagenes/inicio-1.png)

#### Prueba-2:
![Prueba-2 no disponible](https://github.com/phaoliop/BDProject/blob/master/imagenes/inicio-2.png)

