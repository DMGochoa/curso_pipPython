# Curso de Python: PIP y Entornos Virtuales

Para este caso se instala WSl o desde linux se debe asegurar que esta todo debidamente instalado. Por defecto en ambientes de linux esta instalado python. Primero debemos ejecutar los siguientes comandos de actualizacion:

```sh
sudo apt update
sudo apt upgrade
```

Para asegurarnos de tener el gestor de paquetes de python vamos a ejecutar la siguiente linea en la terminal:

```sh
sudo apt install -y python3-pip
```

Por ultimo se instalan estas otras dependencias que son utiles.

```sh
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
```

Para ver la version del gestor pip3

```sh
pip3 -V
```

Al realizar usar un ambiente global se usaria de manera global los modulos y versiones de python. Pero si necesitamos diferentes versiones para cada uno de los proyectos, y si usamos el global solamente, entonces puede llegar a colapsar todo. Es por eso que se necesitan ambientes virtuales que encapsulen diferentes versiones y no lo dejan en zonas compartidas. Es decir que cada proyecto dentra sus propios modulos en diferentes versiones sin que choquen con otros proyectos.

Para empezar usar los ambientes virtuales primero instalamos el paquete python-venv para luego poder empezar a crear ambientes virtuales.

```sh
sudo apt install -y python3-venv
python3 -m venv <env_name>
```

Para activar el ambiente virtual se ejecuta el siguiente comando:

```sh
source env/bin/activate
```

A la hora de instalar librerias dentro del ambiente, mostrar lo que hay instalado y salir del ambiente virtual se usa:

```sh
pip3 install <module_name>
pip3 freeze
deactivate
```

Una forma de guardar los modulos que se usan es al guardarlo en el archivo requirements.txt para guardarlos modulos se usa el comando pip3 freeze de la siguiente forma.

```sh
pip3 freeze > requirements.txt
```

Ahora si se quiere hacer una replica del ambiente virtual se puede usar el archivo requirements.txt para instalar las dependencias que se necesitan.

```sh
pip3 install -r requirements.txt
```

## Docker para encapsular proyectos (tanto la version del python como los modulos)

Vamos hacer dos tipos de dockerizacion es una serie de scripts que se van a ejecutar. Primero se va crear el archivo 'Dockerfile' en la carpeta de app. En donde primero se especifica la version de python, esto para que docker aliste un contenedor con python en esa version instalada. Luego, al ya tener el contenedor se crea una carpeta que va ser el espacio de trabajo. Ahora copiamos ciertos archivos que queremos en el docker, el lado izquierdo es referencia al archivo local y el derecho del lado del contenedor. El siguiente paso es instalar los modulos de python que se van a necesitar en el proyecto, y por ultimo se copia toda la carpeta para guardar en el contenedor en la carpeta especificada.

```dockerfile
FROM python:3.9.12

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD bash -c "while true; do sleep 1; done"
```

Para poder correr el archivo "dockerfile" se crea un nuevo archivo llamado docker-compose.yml en donde se va declarar en que parte y como se va iniciar ese contenedor. Se indica los servicios y el nombre de este, para luego indicar que va construir en la carpeta en la que estoy ubicado, utilizando el archivo "Dockerfile". Una vez establecida la construccion del contenedor, hay que indicar que debe estar encendido (es al estilo de una maquina virtual) por tal motivo se escribe la linea de CMD en el "dockerfile"

```docker-compose.yml
services:
    app-csv:
        build:
            context: .
            dockerfile: Dockerfile
        
```

Para construir el contenedor (Hay que verificar que docker este encendido). Luego de ejecutarlo comienza a construirse, y seguir los pasos especificados.

```sh
docker-compose build
```

Para lanzar docker se escribe la linea de comando de adelante y al final nos indica que se ha creado e iniciado. Luego vemos el estado del contenedor para ver si efectivamente esta en linea. Ahora ingresamos al ambiente para poder desarrollar, le damos ejecutar, el nombre del contenedor y que queremos conectarnos con una terminal tipo bash.

```sh
docker-compose up -d
docker-compose ps
docker-compose exec app-csv bash
```

Para salir del contenedor vamos a usar el comando.

```sh
exit
```

Para bajar el docker.

```sh
docker-compose down
```

## Enlazar el contenedor con tu entorno de desarrollo

Si realizamos un cambio en el proyecto, tocaria que volver hacer un build para poder ver reflejados los cambios. Es por esto que hay que enlazar los sistemas de archivo. Es por esto que en el archivo docker-compose.yml agregamos un volumen en donde decimos que todos los archivos esten enlazados a la carpeta app que esta dentro del contenedor. 

```docker-compose.yml
services:
    app-csv:
        build:
            context: .
            dockerfile: Dockerfile
        volume:
            - .:/app/
```

## Ahora lo que queremos es hacer un contenedor que este siempre encendido para un servidor web

Nos vamos a llevar del proyecto app todo lo que se tiene de docker y se le van a realizar ciertas modificaciones. En el CMD en vez de dejarlo encendido para ejecutar scripts, vamos a lanzar directamente el servidor con uvicorn (esta vez se utiliza otra sintaxis que es con listas).

```dockerfile
FROM python:3.10

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "80]
```

Para el archivo .yml se cambia el nombre de la aplicacion y se hace un enlace de los puertos

```docker-compose.yml
services:
    web-server:
        build:
            context: .
            dockerfile: Dockerfile
        volume:
            - .:/app/
        ports:
            - '80:80'
```
