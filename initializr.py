import os
import pyfiglet
import getpass
import configparser


# == Variables globales ==================
exitApp = False
# ==== Variables del proyecto React============
projectName = ""
projectPath = ""
# ==== Variables Github ==================
githubRepoName = ""
githubUsername = ""
githubPassword = ""
# ==== Archivo de configuracion ==========
config = configparser.ConfigParser()
config.read("script.config")  # leer el archivo de configuración script.config


# Inicializar las variables requeridas
def init():
    projectName = ""


# Logo de React Initialzr
def show_logo():
    print("=".center(65, "="))
    print(pyfiglet.figlet_format("React  Initialzr"))
    print("=".center(65, "="))


# Programa principal
def app():
    global exitApp
    while exitApp is False:
        show_logo()
        exit = input(f"Do you want to exit the app ([Y]es - [N]o)? =>")
        if exit.strip().lower() == "y":
            exitApp = True
            shutdown()


# Proceso para cerrar la aplicación
def shutdown():
    print("Exiting app...")


app()
