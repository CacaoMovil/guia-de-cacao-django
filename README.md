Caja de Herramientas para Cacao
===============
> Aprendiendo e innovando sobre el cacao en sistemas agroforestales

La Caja de Herramientas para Cacao: Aprendiendo e Innovando sobre el Manejo Sostenible del Cultivo de Cacao en Sistemas Agroforestales se compone de 10 guías prácticas para pequeños productores de cacao y sus cooperativas en la región de América Latina.

## Información

El proyecto Caja de Herramientas para Cacao esta elaborado usando el lenguaje de programación [Python](https://www.python.org/) y su framework web [Django](https://www.djangoproject.com/) usando [Postgress](http://www.postgresql.org/) como motor de base de datos, [Redis](http://redis.io/) para el almacenamiento de datos en caché y para la generación de PDF se utilizo [WKHTMLTOPDF](http://http://wkhtmltopdf.org/)

## Instalación

Para poder usar el proyecto es necesario tener instalado las siguiente cosas:

* Python 2.7
* PhantomJS 2.0
* PostgreSQL 9.0
* Redis 3.0
* Pip 7.1
* Virtualenv 13.1

### Instalación de Python

Para poder instalar Python debemos de dirigirnos a la sección de [descargas del lenguaje de programación](https://www.python.org/downloads/) y elegir la versión que necesitamos para el sistema operativo que estemos usando.

Por defecto todos los sistemas operativos que parten del Kernel de Linux traen por defecto Python instalado, por otra parte todas las versiones de OSX igualmente traer instalado Python por defecto. Si cuenta con otro sistema operativo por favor dirijase a la sección de descargas y siga los pasos que ahí le recomiendan.

Para verificar que tenemos instalado Python, basta con ejecutar la siguiente instrucción en la línea de comandos:
	python -V

### Instalación de WKHTMLTOPDF

Para instalar WKHTMLTOPDF descarge el paquete desde la sección de [descargas](http://wkhtmltopdf.org/downloads.html) extraiga los datos contenidos en el paquete e instale.

### Instalación de PostgreSQL

Para instalar PostgreSQL dirijase a la sección de [descargas](http://www.postgresql.org/download/) y seleccion el paquete requerido para su entorno.

### Instalación de Redis

Dirigase a la sección de [descargas de Redis](http://redis.io/download) una ves descargado, extraiga toda la información contenida dentro del paquete y en la línea de comandos ejecute las siguientes instrucciones:

	cd redis-stable
	make

### Instalación de Pip

Como ya tiene instalado Python solo necesitamos ejecutar lo siguiente en la línea de comandos:

	sudo apt-get install python-setuptools python-dev build-essential
	sudo easy_install pip

### Instalación de Virtualenv

Para poder instalar virtualenv es necesario haber instalado Pip y tener Python en el entorno, Virtualenv es instalado mediante PIP, para ello ejecuta el siguiente comando:

	sudo pip install virtualenv

En este paso también instalaremos VirtualenvWrapper que es sólo una utilidad o envoltura alrededor virtualenv que hace que sea aún más fácil trabajar con el.

	sudo pip install virtualenvwrapper

Para utilizar virtualenvwrapper debe añadir dos líneas a su archivo de inicio de shell (por ejemplo, .bash_profile):

	export WORKON_HOME=$HOME/.virtualenvs
	source /usr/local/bin/virtualenvwrapper.sh

## Configuracion

Una ves instalado todas las dependencias, procederemos a configurar el proyecto, para ello crearemos la base de datos

	createdb cacao_app

Crearemos un entorno virtual para poder alojar todas las dependencias del proyecto y que no interfiera con nuestro sistema

	mkvirtualenv cacao

Una ves creado el entorno necesitamos instalar las dependencias

	pip install -r requirements.txt

Seguidamente procederemos a migrar todos nuestro datos ejecutando lo siguiente:

	python manage.py syncdb

Necesitamos iniciar nuestro servidor redis en otra instancia de nuestra línea de comando

	redis-server

El proyecto cuenta con un archivo para configurar variables de entorno (.env) este archivo nos brinda seguridad debido a que
nuestros datos no son visibles para otros usuarios, recuerde mantener su archivo (.env) seguro y sea cuidadoso con quien lo
comparte.

Actualmente hay dos variables de entorno que son requeridas para poder ejecutar el proyecto:

- Facebook APP ID
- Google App ID

Este es un ejemplo de como es el archivo para variables de entorno:

```bash
DJANGO_GA_APP_ID=1234
DJANGO_FB_APP_ID=1234
```

Recuerde cambiar los valores por defecto que poseen, anteponer la palabra 'DJANGO' y escribirlas en su preferencia en mayusculas.


Ahora corremos el servidor de django

	python manage.py runserver

Entra desde tu navegador a la dirección [localhost:8000](http:localhost:8000) para ver el proyecto

## Edición de estilos

Existen diferentes maneras de modificar el estilo de este proyecto, y dependera mucho del requerimiento que se desee cumplir como producto final.

### Estilos Básicos

La manera mas fácil es agregando un nuevo archivo ```.css``` con reglas que sobre escriban las existentes. 
Esta es una solución muy util para casos en donde se requieran realizar cambios minimos a los estilos actuales.

A continuación se listan las importaciones de archivos de estilos actuales y se muestra un ejemplo de como debe agregarse al final de la lista, el archivo con los estilos propios. En este caso el archivo con estilos personalizados se le ha llamado ```custom-project.css```.

```
<!-- Application stylesheet -->
<link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
<link rel="stylesheet" href="{% static 'css/layout.min.css' %}">
<link rel="stylesheet" href="{% static 'css/uielement.min.css' %}">
<link rel="stylesheet" href="{% static 'css/custom.css' %}">
<link rel="stylesheet" href="{% static 'css/colors-guias.min.css' %}">
<!--/ Application stylesheet -->

<!-- Custom styles for project-->
<link rel="stylesheet" href="{% static 'css/custom-project.css' %}">

```

Este archivo debe ser agregado en las plantillas ```base.html``` y ```guide_detail_base.html```.

### Estilos Avanzados

Los estilos del proyecto son generados a partir de la edición de archivos ```.less``` que se encuentran ubicados en el directorio ```/static/less```. Estos archivos luego de ser compilados, se generan en sus versiones respectivas ```.css```. Less es un preprocesador de css, para mayor información sobre su sintaxis en [lesscss.org](http://lesscss.org/)


Dentro del directorio ```/static/``` se encuentra un archivo ```Gruntfile.js``` el cual contiene todas las tareas de ***Grunt*** necesarias para compilar los archivos de estilo. Para mayor información [gruntjs.com](http://gruntjs.com/)

Es requerido tener instalado ***npm***, para mayor información [npm.js](https://www.npmjs.com/)

Para instalar ***Grunt*** y todas sus dependencias, se debe ubicarse dentro del directorio ```/static/``` y ejecutar el comando:

```$ npm install ```

Finalmente iniciar Grunt.

```$ grunt```

Mientras ***Grunt*** este corriendo, cualquier cambio que se realice sobre los archivos ```.less```, disparara la tarea de Grunt que compila los archivos a sus versiones minificadas ```.css```.

### Colores personalizados para guías.

Se pueden definir colores personalizados para cada guía. Se tienen colores predefinidos en los estilos del proyecto para las 10 primeras guías de documentos. Por lo cual se si desea editar esos colores o agregar nuevos, se debe seguir el siguiente proceso.

En primera instancia es requerido, tener lista la configuración para editar archivos ```.less``` que fue explicado en el punto anterior (Estilos avanzados).

En el archivo ```/static/less/variables.less``` y ubicar la sección en donde se definen las variables para los colores de cada guía.

```
// color guias
@colors:								10;
@color-guia-default:					#56687F;							
@color-guia1:							#872058;
@color-guia2:							#7A132C;
@color-guia3:							#26799B;
@color-guia4:							#894C1D;
@color-guia5:							#DC661E;
@color-guia6:							#918144;
@color-guia7:							#5F2E23;
@color-guia8:							#991A72;
@color-guia9:							#C01772;
@color-guia10:							#CD8739;
```

Basicamente se debe editar cada variable con el color deseado. En caso de requerir colores para mayor de 10 guías, deben agregarse consecutivamente de la misma forma como estan definidas actualmente y tambien cambiar el valor de la variable ```@colors``` con el valor total de las guías que requieran colores personalizados. En el caso de no necesitar definir colores adicionales, se usa para todas las guías el color definido en la variable ```@color-guia-default: #56687F;```.

El archivo ```css/colors-guias.min.css``` esta agregado en las plantillas ```base.html``` y ```guide_detail_base.html```.

```
<link rel="stylesheet" href="{% static 'css/colors-guias.min.css' %}">
```

En el caso de no requerir estilos personalizados para cada guía solo se debe eliminar la importación a este archivo, y las guías utilizarían el color por defecto.

## Contribución

Si quieres contribuir a este proyecto, por favor, lea el archivo de contribuyentes y realice los siguientes pasos

    # Fork this repository
    # Clone your fork
    make run

    git checkout -b feature_branch
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send a pull request for your feature branch

## Licencia

Caja de Herramientas para Cacao: Aprendiendo e Innovando sobre el Manejo Sostenible del Cultivo de Cacao en Sistemas Agroforestales por Lutheran World Relief se distribuye bajo una [Licencia Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional.](http://creativecommons.org/licenses/by-nc-sa/4.0/deed.es)

El código de la aplicación Cacao Móvil y su versión web han sido liberados bajo Licencia Pública General de GNU versión 3 (GPLv3)
