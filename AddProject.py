from checkUserData import checkUniqueProjectId
from datetime import datetime
from InsertProjectData import insertProjectInfo
def addProject(usrMail):
    print("----------------------- ADD PROJECT -----------------------")
    projectId = input("please enter your project ID: ")
    while True:
        if projectId.isnumeric():
            if checkUniqueProjectId(projectId):
                break
        else:
            projectid = input("invalid field, please enter your project ID: ")
######################################################################################################################
    projectTitle = input("please enter your project title: ")
    while True:
        if projectTitle.isalpha():
            break
        else:
            projectTitle = input("invalid field, please enter your project title: ")
######################################################################################################################
    projectDetails = input("please enter your project details: ")
    while True:
        if projectDetails:
            break
        else:
            projectDetails = input("invalid field, please enter your project details: ")
######################################################################################################################
    projectTarget = input("please enter your project target: ")
    while True:
        if projectTarget.isnumeric():
            break
        else:
            projectTarget = input("invalid field, please enter your project target: ")
######################################################################################################################
    while True:
        projectStartDate = input("please enter your project start date in format yyyy-mm-dd: ")
        if projectStartDate:
            isValidDate = True
            try:
                BeginDate = datetime.strptime(projectStartDate, "%Y-%m-%d")
            except ValueError:
                isValidDate = False
                print("Input date is not valid..")
                continue
            break
        else:
            projectStartDate = input("invalid field, please enter your project start date in format yyyy-mm-dd: ")
######################################################################################################################
    while True:
        projectEndDate = input("please enter your project end date in format yyyy-mm-dd: ")
        if projectEndDate:
            isValidDate = True
            try:
                EndDate = datetime.strptime(projectEndDate, "%Y-%m-%d")
            except ValueError:
                isValidDate = False
                print("Input date is not valid..")
                continue
            break
        else:
            projectEndDate = input("invalid field, please enter your project end date in format yyyy-mm-dd: ")
######################################################################################################################
    info = [usrMail,projectId, projectTitle, projectDetails, projectTarget, projectStartDate, projectEndDate]
    proj_info = ":".join(info)
    insertProjectInfo(proj_info)