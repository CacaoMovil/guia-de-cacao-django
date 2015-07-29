Caja de Herramientas para Cacao
===============
> Aprendiendo e innovando sobre el cacao en sistemas agroforestales

La Caja de Herramientas para Cacao: Aprendiendo e Innovando sobre el Manejo Sostenible del Cultivo de Cacao en Sistemas Agroforestales se compone de 10 guías prácticas para pequeños productores de cacao y sus cooperativas en la región de América Latina.

## Información

El proyecto Caja de Herramientas para Cacao esta elaborado usando el lenguaje de programación [Python](https://www.python.org/) y su framework web [Django](https://www.djangoproject.com/) usando [Postgress](http://www.postgresql.org/) como motor de base de datos, [Redis](http://redis.io/) para el almacenamiento de datos en caché y para la generación de PDF se utilizo [PhantomJS](http://phantomjs.org/)

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

### Instalación de PhantomJS

Para instalar PhantomJS descarge el paquete desde la sección de [descargas](http://phantomjs.org/download.html) extraiga los datos contenidos en el paquete e instale.

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

Ahora corremos el servidor de django

	python manage.py runserver

Entra desde tu navegador a la dirección [localhost:800](http:localhost:8000) para ver el proyecto

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
