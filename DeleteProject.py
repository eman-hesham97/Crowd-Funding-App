def deleteProject(usrMail):
    print("----------------------- DELETE PROJECT -----------------------")
    print("Here's a list of all your projects:\n")
    newList = []
    with open("Projects.txt", 'r') as pfile:
        projects = pfile.readlines()
        for proj in projects:
            proj_info = proj.split(":")
            newList.append(proj_info)
            if proj_info[0] == usrMail:
                print(proj_info)
    #--------------------------------------------------------------------
    myProjID = input("enter id of project you want to delete: ")
    if myProjID.isnumeric():
        for pos,i in enumerate(newList):
            print(pos,i)
            print(i[1])
            if i[1] == myProjID:
                newList[pos].clear()
                print(newList[pos])
                with open("Projects.txt", 'w') as pfile:
                    with open("Projects.txt", "a") as pfile:
                        for i in newList:
                            pfile.write(":".join(i))

    else:
        myProj = input("invalid field, please enter your project ID: ")
    return True