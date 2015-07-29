Caja de Herramientas para Cacao
===============
> Aprendiendo e innovando sobre el cacao en sistemas agroforestales

La Caja de Herramientas para Cacao: Aprendiendo e Innovando sobre el Manejo Sostenible del Cultuvo de Cacao en Sistemas Agroforestales se compone de 10 guías prácticas para pequeños productores de cacao y sus cooperativas en la región de América Latina.

## Informacion

El projecto Caja de Herramientas para Cacao esta elaborado usando el lenguaje de programacion [Python](https://www.python.org/) y su framework web [Django](https://www.djangoproject.com/) usando [Postgress](http://www.postgresql.org/) como motor de base de datos, [Redis](http://redis.io/) para el almacenamiento de datos en cache y para la generacion de PDF se utilizo [PhantomJS](http://phantomjs.org/)

## Instalacion

Para poder usar el projecto es necesario tener instalado las siguiente cosas:

* Python 2.7 
* PhantomJS 2.0
* PostgreSQL 9.0
* Redis 3.0
* Pip 7.1
* Virtualenv 13.1

### Instalacion de Python

Para poder instalar Python debemos de dirigirnos a la seccion de [descargas del lenguaje de programacion](https://www.python.org/downloads/) y elejir la version que necesitamos para el sistema operativo que estemos usando.

Por defecto todos los sistemas operativos que parten del Kernel de Linux traen por defecto Python instalado, por otra parte todas las versiones de OSX igualmente traer instalado Python por defecto. Si cuenta con otro sistema operativo por favor dirijase a la seccion de descargas y siga los pasos que ahi le recomiendan.

Para verficar que tenemos instalado Python, basta con ejecutar la siguiente instruccion en la linea de comandos:
	python -V 

### Instalacion de PhantomJS

Para instalar PhantomJS descarge el paquete desde la seccion de [descargas](http://phantomjs.org/download.html) extraiga los datos contenidos en el paquete e instale.

### Instalacion de PostgreSQL

Para instalar PostgreSQL dirijase a la seccion de [descargas](http://www.postgresql.org/download/) y seleccion el paquete requerido para su entorno.

### Instalacion de Redis

Dirigase a la seccion de [descargas de Redis](http://redis.io/download) una ves descargado, extraiga toda la informacion contenida dentro del paquete y en la linea de comandos ejecute las siguientes instrucciones:
	
	cd redis-stable
	make

### Instalacion de Pip

Como ya tiene instalado Python solo necesitamos ejecutar lo siguiente en la linea de comandos:

	sudo apt-get install python-setuptools python-dev build-essential 
	sudo easy_install pip

### Instalacion de Virtualenv

Para poder instalar virtualenv es necesario haber instalado Pip y tener Python en el entorno, Virtualenv es instalado mediante PIP, para ello ejecuta el siguiente comando:

	sudo pip install virtualenv 

En este paso tambien instalaremos VirtualenvWrapper que es sólo una utilidad o envoltura alrededor virtualenv que hace que sea aún más fácil trabajar con el.
	
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

Necesitamos inicar nuestro servidor redis en otra instancia de nuestra linea de comando
	
	redis-server

Ahora corremos el servidor de django

	python manage.py runsever

Entra desde tu navegador a la direccion [localhost:800](http:localhost:8000) para ver el proyecto

## Contribucion

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
