def editProject(usrMail):
    print("----------------------- EDIT PROJECT -----------------------")
    print("Here's a list of all your projects:\n")
    newList = []
    with open("Projects.txt", 'r') as pfile:
        projects = pfile.readlines()
        for proj in projects:
            proj_info = proj.split(":")
            newList.append(proj_info)
            if proj_info[0] == usrMail:
                print(proj_info)
    #------------------------------------------------------------------
    myProjID = input("enter id of project you want to edit: ")
    if myProjID.isnumeric():
        flag = False
        myProjID = int(myProjID)
        for i in newList:
            if int(i[1]) == myProjID:
                g = input("please enter one of the following options\n"
                          "'a' to edit project title\n'b' to edit project details\n"
                          "'c' to edit project target\n'd' to edit project start date"
                          "\n'e' to edit project end date : ")
                if g == "a":
                    h=input("enter new title: ")
                    while True:
                        if h.isalpha():
                            i[2] = h
                            # print(i)
                            flag = True
                            with open("Projects.txt", 'w') as pwfile:
                                #projects = pwfile.readlines()
                                for lst in newList:
                                    lst= ":".join(lst)
                                    pwfile.write(lst)
                                    pwfile.write("\n")
                            break
                        else:
                            h = input("invalid value, enter new title: ")
                elif g == 'b':
                    h = input("enter new project details: ")
                    while True:
                        if h.isalpha():
                            i[3] = h
                            flag = True
                            with open("Projects.txt", 'w') as pwfile:
                                for lst in newList:
                                    lst = ":".join(lst)
                                    pwfile.write(lst)
                                    pwfile.write("\n")
                            break
                        else:
                            h = input("invalid value, enter new project details: ")
                elif g == 'c':
                    h = input("enter new project target: ")
                    while True:
                        if h.isnumeric():
                            i[4] = h
                            flag = True
                            with open("Projects.txt", 'w') as pwfile:
                                for lst in newList:
                                    lst = ":".join(lst)
                                    pwfile.write(lst)
                                    pwfile.write("\n")
                            break
                        else:
                            h = input("invalid value, enter new project target: ")
                elif g == 'd':
                    h = input("enter new project start date in format yyyy-mm-dd: ")
                    while True:
                        if h:
                            i[5] = h
                            flag = True
                            with open("Projects.txt", 'w') as pwfile:
                                for lst in newList:
                                    lst = ":".join(lst)
                                    pwfile.write(lst)
                                    pwfile.write("\n")
                            break
                        else:
                            h = input("invalid value, enter new project start date in format yyyy-mm-dd: ")
                elif g == 'e':
                    h = input("enter new project end date in format yyyy-mm-dd: ")
                    while True:
                        if h:
                            i[6] = h
                            flag = True
                            with open("Projects.txt", 'w') as pwfile:
                                for lst in newList:
                                    lst = ":".join(lst)
                                    pwfile.write(lst)
                                    pwfile.write("\n")
                            break
                        else:
                            h = input("invalid value, enter new project end date in format yyyy-mm-dd: ")
                else:
                     print("invalid option")

                if flag == True:

                    break
    else:
        myProj = input("invalid field, please enter your project ID: ")
    return True