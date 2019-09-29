import os
import pyfiglet
import getpass
import configparser
import re

# == Variables globales ====================================
exitApp = False
decoratorLength = 65
decoratorSymbol = "="
# ==== Archivo de configuracion ===========================
config = configparser.ConfigParser()
config.read("app.config")
# ==== Variables del proyecto React=========================
projectName = ""
projectPath = config.get("DEFAULT", "directory")
# ==== Variables Github ====================================
githubRepoName = ""
githubUsername = ""
githubPassword = ""

# ==== Variables de editor ================================
editor = ""  # leer el archivo de configuración app.config

# ==== Workflow de la aplicación ==========================
# 1. Inicializar variables del proyecto
# 2. Crear el proyecto React.js con create-react-app
# 4. Crear un repositorio en Github y subir el proyecto
# 5. Iniciar el editor de texto
# 6. Iniciar el servidor React.JS en localhost


# Inicializar las variables requeridas
def init_project(projName, projPath):
    global projectPath
    projectPath = projPath
    global projectName
    projectName = projName


def separator():
    print("=".center(decoratorLength, decoratorSymbol))


# Logo de React Initialzr
def show_logo():
    separator()
    print(pyfiglet.figlet_format("React  Initialzr"))
    separator()


# Programa principal
def app():

    show_logo()
    global exitApp
    while exitApp is False:
        # fase para definir ubicación y nombre del proyecto
        print("// Fase 1 //")

        # Caracteres inválidos \ / < > : ! * | ?
        proj = input("Escriba el nombre el proyecto React.js ==> ").strip()

        while re.findall(r"[\\/<>:!*|?.]", proj):
            print(
                "El nombre de proyecto no puede contener los caracteres: \ / < > : ! * . | ?")
            proj = input(
                "Introduzca otro nombre para el proyecto React.js ==> ").strip()

        if(projectPath == ""):
            print("No hay una ruta de proyecto por defecto especificada")
            projPath = input("Introduzca una ruta de directorio ==> ")
            init_project(proj.strip(), projectPath)

        separator()
        print("// Fase 2 //")

        exit = input(f"Desea crear otro proyecto? ([Y]es - [N]o)? ==>")
        if exit.strip().lower() == "n":
            exitApp = True
            shutdown()


# Proceso para cerrar la aplicación
def shutdown():
    print("Cerrando aplicación...")


app()
