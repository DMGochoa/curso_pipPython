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
