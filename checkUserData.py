def checkData(userMail, password):
    with open("Users.txt") as rfile:
        users = rfile.readlines()
        for user in users:
            user_info = user.split(":")
            if user_info[2] == userMail and user_info[3] == password:
                return True
    return False

def checkUniqueMail(registerMail):
    with open("Users.txt") as rfile:
        users = rfile.readlines()
        for user in users:
            user_info = user.split(":")
            if user_info[2] == registerMail:
                print("repeated mail")
                exit()
    return True

def checkUniqueProjectId(projectId):
    with open("Projects.txt") as pfile:
        projects = pfile.readlines()
        for proj in projects:
            proj_info = proj.split(":")
            if proj_info[0] == projectId:
                print("repeated project id")
                exit()
    return True