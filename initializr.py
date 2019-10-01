import os
import pyfiglet
import getpass as gp
import configparser
import re
import subprocess
from github import Github

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
githubUsername = config.get("DEFAULT", "username")
githubPassword = config.get("DEFAULT", "password")

# Variables de editor
defaultEditor = config.get("DEFAULT", "editor")

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
    global projectPath
    projectPath = os.path.join(workspacePath, projectName)


def create_react_app():
    subprocess.check_call(
        "npx create-react-app {}".format(projectPath).lower(), shell=True)


def GetGithubCredentials():
    global githubUsername
    while not githubUsername:
        print("No hay un usuario Github por defecto configurado")
        githubUsername = input("Introduzca su usuario Github ==>").strip()

    global githubPassword
    while not githubPassword:
        print("No hay una contraseña Github por defecto configurada")
        githubPassword = gp.getpass(
            prompt="Introduzca su contraseña Github ==>", stream=None)


def CreateGithubRepo():
    global githubUsername
    global githubPassword
    global githubRepoName

    try:
        GetGithubCredentials()
        githubRepoName = input(
            "Introduzca el nombre del repositorio Github ==>")
        print("Creando repositorio Github...")
        account = Github(githubUsername, githubPassword).get_user()
        account.create_repo(githubRepoName)
        return True
    except Exception as e:
        githubUsername = ""
        githubPassword = ""
        print("Hubo un error al crear el repositorio Github")
        DeleteGitHubRepo()
        return False


def DeleteGitHubRepo():
    print("Eliminando repositorio Github...")

    global githubUsername
    global githubPassword
    global githubRepoName

    try:
        user = Github(githubUsername, githubPassword)
        repo = user.get_repo("{}/{}".format(githubPassword, githubRepoName))
        repo.delete()
        print("Repositorio Github eliminado!")
    except Exception as e:
        print(str(e))
        print("""
        No se puedo eliminar el repositorio \'{}\'. Elimínelo manualmente.
        """.format(
            repoName))


# Proceso para cerrar la aplicación
def shutdown():
    print("Cerrando aplicación...")


# Programa principal
def app():
    show_logo()

    global exitApp
    global workspacePath
    global projectName
    global githubUsername
    global githubRepoName

    while exitApp is False:
        # fase para definir ubicación y nombre del proyecto
        print("// Fase 1 //")

        proj = input("Escriba el nombre del proyecto React.js ==> ").strip()

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

        print(f"Creando proyecto {projectName} en {projectPath}...")

        os.chdir(workspacePath)

        create_react_app()
        print("Proyecto React.js creado!")

        print("// Fase 3 //")

        while not CreateGithubRepo():
            print("Hubo un error al crear el repositorio Github, intente de nuevo")

        try:
            print(projectPath)
            os.chdir(projectPath)

            # Si el repositorio se creó ejecutar versionamiento en Git
            # subprocess.call("git init", shell=True)
            subprocess.call("git add .", shell=True)
            subprocess.call('git commit -m "initial commit"', shell=True)
            subprocess.call(
                f"git remote add origin https://github.com/{githubUsername}/{githubRepoName}", shell=True)
            subprocess.call("git push -u origin master", shell=True)

            print("Proyecto Github versionado correctamente")

        except Exception as e:
            print("Hubo un error al versionar el proyecto Github")
            print(e)

        print("// Fase 4 //")

        # Si el proyecto se versiona correctamente iniciar el editor
        if not defaultEditor:
            print("No hay un editor por defecto configurado.")
        else:
            print("Iniciando editor {}...".format(defaultEditor))
            subprocess.call("{} .".format(defaultEditor), shell=True)

        print("// Fase 5 //")

        # Iniciar el servidor React
        print("Iniciando el servidor...")
        subprocess.check_call("npm start", shell=True)
        print("Servidor iniciado! En breve se abrirá una pestaña en su navegador")

        exit = input(f"Desea crear otro proyecto? ([Y]es - [N]o)? ==>")
        if exit.strip().lower() == "n":
            exitApp = True
            shutdown()


app()
