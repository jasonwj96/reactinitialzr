# Importar la imagen de Python 3 en Docker Hub
FROM python:3.7
# Añadir el archivo del programa en la carpeta app
ADD app.py /
ADD script.config /
# Importar las dependencias del program
RUN pip install PyGithub
RUN pip install configparser 
RUN pip install pyfiglet
# Actualizar 
RUN apt-get update
# install curl 
RUN apt-get install curl
# get install script and pass it to execute: 
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash
# Instalar git
RUN apt-get install git
# and install node 
RUN apt-get install nodejs
# confirm that it was successful 
RUN node -v 
# npm installs automatically 
RUN npm -v
# Instalar create react app
RUN npm i -g create-react-app
# Crear directorio por defecto para los proyectos
RUN mkdir Projects
# Definir el comando por defecto que se ejecutará al crearse el contenedor
CMD [ "python", "app.py" ]

