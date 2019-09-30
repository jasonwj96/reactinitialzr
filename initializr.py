import os
import pyfiglet
import getpass
import configparser
import re
import subprocess

# Variables globales
exitApp = False
decoratorLength = 65
decoratorSymbol = "="
# Archivo de configuracion
config = configparser.ConfigParser()
config.read("app.config")
# Variables del proyecto React
projectName = ""
projectPath = ""
workspacePath = config.get("DEFAULT", "directory")
# Variables Github
githubRepoName = ""
githubUsername = ""
githubPassword = ""

# Variables de editor
editor = ""  # leer el archivo de configuración app.config

# Workflow de la aplicación
# 1. Inicializar variables del proyecto
# 2. Crear el proyecto React.js con create-react-app
# 4. Crear un repositorio en Github y subir el proyecto
# 5. Iniciar el editor de texto
# 6. Iniciar el servidor React.JS en localhost


def separator():
    print("=".center(decoratorLength, decoratorSymbol))


# Logo de React Initialzr
def show_logo():
    separator()
    print(pyfiglet.figlet_format("React  Initialzr"))
    separator()


# Inicializar las variables requeridas
def init_project(projName, workPath):
    global workspacePath
    workspacePath = workPath
    global projectName
    projectName = projName


def create_react_app():
    subprocess.check_call(
        "npx create-react-app {}".format(os.path.join(workspacePath, projectName).lower()), shell=True)


# Programa principal
def app():

    show_logo()
    global exitApp
    while exitApp is False:
        # fase para definir ubicación y nombre del proyecto
        print("-- Fase 1 --")

        proj = input("Escriba el nombre el proyecto React.js ==> ").strip()

        # Caracteres inválidos en Windows, Linux y MacOS: \ / < > : ! * | ?
        while re.findall(r"[\\/<>:!*|?.\"]", proj):
            print(
                r"El nombre de proyecto no puede contener los caracteres: \" \ / < > : ! * . | ?")
            proj = input(
                "Introduzca otro nombre para el proyecto React.js ==> ").strip()

        # Si no hay un directorio de trabajo por defecto se debe ingresar uno
        if not workspacePath:
            # Verifica que el directorio de trabajo exista
            print("No hay una ruta de proyecto por defecto especificada")
            workPath = input("Introduzca una ruta de directorio ==> ")

            while not os.path.isdir(workPath):
                print("La ruta del espacio de trabajo no es válida.")
                workPath = input("Ingrese una ruta nueva ==> ")

            # Inicializar variables del proyecto
            init_project(proj.strip(), workPath)
        else:
            init_project(proj.strip(), workspacePath)

        separator()
        print("// Fase 2 //")

        print(f"Creando proyecto {projectName}...")
        os.chdir(workspacePath)
        create_react_app()
        print("Proyecto React.js creado!")

        exit = input(f"Desea crear otro proyecto? ([Y]es - [N]o)? ==>")
        if exit.strip().lower() == "n":
            exitApp = True
            shutdown()


# Proceso para cerrar la aplicación
def shutdown():
    print("Cerrando aplicación...")


app()
