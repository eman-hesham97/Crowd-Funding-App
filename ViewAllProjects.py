def viewProjects():
    print("----------------------- ALL PROJECTS -----------------------")
    with open("Projects.txt", 'r') as pfile:
        projects = pfile.readlines()
        for proj in projects:
            proj_info = proj.split(":")
            print(proj_info)
    return True