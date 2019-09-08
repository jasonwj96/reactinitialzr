import os
import subprocess
from github import Github
import configparser

# configure parser for script.config
config = configparser.ConfigParser()
config.read("script.config")

# global variables
projectName = ""
repoName = ""
repoName = ""
# get default credentials from script.config file
username = config.get("DEFAULT", "username")
password = config.get("DEFAULT", "password")
# project variables
directory = config.get("DEFAULT", "directory")
editor = config.get("DEFAULT", "editor")
projectName = ""
projectType = ""


# Initializes global variables
def Init(project, repo):
    global projectName
    global repoName
    projectName = project
    repoName = repo


# This process calls create-react-app to create a new React project
# given a project name
def React():
    subprocess.check_call(
        "npx create-react-app {}".format(projectName), shell=True)
    os.chdir(projectName)

    Init(projectName, repoName)


# Gets the user's Github credentials to create a new repository
def GetCredentials():
    global repoName
    global username
    global password
    repoName = input("Enter a name for the GitHub repository: ")

    if (username == ""):
        # TODO: replace this with electron GUI
        username = input("Enter your GitHub username: ")
    if (username == "" or password == ""):
        # TODO: replace this with electron GUI
        password = getpass.getpass("Enter your GitHub password: ")


# creates GitHub repositort if the credentials given are valid
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
        print("""Could not delete new repository \'{}\'. Delete it 
        online.""".format(repoName))


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
projectName = input("Project name: ")


# loops until there is a valid project name
while os.path.isdir(directory + "\\" + projectName):
    print("Project name already exists, please try again.")
    projectName = input("Project name: ")


# requests user for project type
# projectType = input("Project type: ")


# loops until project type is valid  # TODO: refactor this
# while projectType not in project_types.types:
#     print("{}Invalid project type; please try again.{}".format(
#         Fore.YELLOW, Fore.WHITE))
#     print("Valid project types: ")
#     for key, value in project_types.types.items():
#         print(Fore.BLUE + key + Fore.WHITE)
#     projectType = input("Project type: ")


# loops until GitHub repo has been created successfully
while CreateGitHubRepo() is False:
    print("Something went wrong when creating the GitHub repo")

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
            print("No editor found: {}".format(str(e)))

    else:
        print("No editor selected.")
        print("Project created succesfully!")

    # starts dev server for react projects
    subprocess.call("npm start", shell=True)

except Exception as e:
    print("There was an error when creating the project:{}")
    DeleteGitHubRepo()
