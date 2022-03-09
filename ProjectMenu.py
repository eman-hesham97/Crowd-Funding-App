from AddProject import addProject
from ViewAllProjects import viewProjects
from EditProject import editProject
from DeleteProject import deleteProject

def projectMenu(usrMail):
    y = input("please enter one of the following options\n"
              "'a' for adding a new project\n'v' for viewing all projects\n"
              "'e' for editing a project\n'd' for deleting a project : ")
    if y == 'a':
        addProject(usrMail)
    elif y == 'v':
        viewProjects()
    elif y == 'e':
        editProject(usrMail)
    elif y == 'd':
        deleteProject(usrMail)
    else:
        print("invalid option")
        projectMenu(usrMail)