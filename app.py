import os
import subprocess
from github import Github
import configparser
import pyfiglet
import getpass


# configure parser para el script.config
config = configparser.ConfigParser()
config.read("script.config")

# variables globales
projectName = ""
repoName = ""
repoName = ""
username = config.get("DEFAULT", "username")
password = config.get("DEFAULT", "password")
directory = config.get("DEFAULT", "directory")
editor = config.get("DEFAULT", "editor")
projectName = ""
projectType = ""
exitApp = false


# Inicializa las variables globales
def Init(project, repo):
    global projectName
    global repoName
    projectName = project
    repoName = repo


# Proceso para crear nueva aplicación react
def React():
    subprocess.check_call(
        "npx create-react-app {}".format(projectName), shell=True)
    os.chdir(projectName)

    Init(projectName, repoName)


# Proceso para obtener credenciales Github
def GetCredentials():
    global repoName
    global username
    global password
    repoName = input("Introduzca un nombre para el repositorio Github: ")

    if (username == ""):
        username = input("Introduzca su usuario de Github: ")
    if (username == "" or password == ""):
        password = getpass.getpass(prompt="""
        Introduzca su contraseña de GitHub: """, stream=None)


# Proceso que crea el repositorio Github si las credenciales son válidas
def CreateGitHubRepo():
    global repoName
    global username
    global password
    GetCredentials()
    try:
        user = Github(username, password).get_user()
        user.create_repo(repoName)
        return True
    except Exception as e:
        username = ""
        password = ""
        print(e)
        return False


def DeleteGitHubRepo():
    global repoName
    global username
    global password
    try:
        user = Github(username, password)
        repo = user.get_repo("{}/{}".format(username, repoName))
        repo.delete()
    except Exception as e:
        print(str(e))
        print("""No se puedo eliminar el repositorio \'{}\'. Elimínelo manualmente.""".format(
            repoName))


# Programa principal
while exitApp == false:
    print("=".center(65, "="))
    print(pyfiglet.figlet_format("React  Initialzr"))
    print("=".center(65, "="))

    # loops until there is a valid file path
    if not os.path.isdir(directory):
        print("""Invalid string for the directory option in script.config;
        please make sure the directory in script.config exists
        to stop seeing this message in
        the future.""")

        directory = input("Enter valid local path: ")

        while not os.path.isdir(directory):
            print("Invalid local path; please try again.")
            directory = input("Enter valid local path: ")

    # requests user for project name
    projectName = input("Nombre del proyecto: ")

    # loops until there is a valid project name
    while os.path.isdir(directory + "\\" + projectName):
        print("Error: el nombre del proyecto ya existe, introduzca otro.")
        projectName = input("Nombre del proyecto: ")

    # loops until GitHub repo has been created successfully
    while CreateGitHubRepo() is False:
        print("Hubo un error al crear el repositorio Github")

    try:
        # changes into correct directory and runs the project process
        os.chdir(directory)
        React()

        # git proccesses
        subprocess.call("git init", shell=True)
        subprocess.call("git add .", shell=True)
        subprocess.call("git commit -m \"initial commit\"", shell=True)
        subprocess.call(
            """git remote add origin https://github.com/{}
            /{}""".format(username, repoName), shell=True)
        subprocess.call("git push -u origin master", shell=True)

        # opens project in editor
        if editor is not "none":
            try:
                subprocess.call("{} .".format(editor), shell=True)

            except Exception as e:
                print("No se encontró un editor: {}".format(str(e)))

        else:
            print("No editor selected.")
            print("Project created succesfully!")

        # starts dev server for react projects
        subprocess.call("npm start", shell=True)

    except Exception as e:
        print("Hubo un error al crear el proyecto:{}")
        DeleteGitHubRepo()

    answer = input("Desea crear otro repositorio? (Y/n)")
    if(answer == "n"):
        exitApp = true
        print("Cerrando la aplicación...")
