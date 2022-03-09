def insertProjectInfo(info):
    with open("Projects.txt", "a") as pfile:
        data = info.strip("\n")
        data=f"{data}\n"
        pfile.write(data)
        pfile.close()